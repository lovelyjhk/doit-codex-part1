import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const here = path.dirname(fileURLToPath(import.meta.url));
const allowedRoot = path.resolve(here, "..");
const allowedRootReal = await fs.realpath(allowedRoot);

async function safePath(relativePath) {
  const target = path.resolve(allowedRoot, relativePath);
  if (target !== allowedRoot && !target.startsWith(`${allowedRoot}${path.sep}`)) {
    throw new Error("허용된 실습 폴더 밖의 파일은 읽을 수 없습니다.");
  }
  const targetReal = await fs.realpath(target);
  if (targetReal !== allowedRootReal && !targetReal.startsWith(`${allowedRootReal}${path.sep}`)) {
    throw new Error("링크나 정션을 거쳐 허용된 실습 폴더 밖의 파일은 읽을 수 없습니다.");
  }
  return targetReal;
}

function inspect(text) {
  const findings = [];
  text.split(/\r?\n/).forEach((line, index) => {
    if (/ {2,}/.test(line)) findings.push({line:index+1,type:"반복 공백",text:line});
    if (/[.!?]{2,}/.test(line)) findings.push({line:index+1,type:"연속 문장부호",text:line});
    if (/\[\s*\]/.test(line)) findings.push({line:index+1,type:"빈 대괄호",text:line});
    if (/계약 한다|지급 한다/.test(line)) findings.push({line:index+1,type:"띄어쓰기 후보",text:line});
    if (/편집화일|카드 뉴스/.test(line)) findings.push({line:index+1,type:"용어 표기 후보",text:line});
  });
  return findings;
}

const server = new McpServer({name:"readonly-document-check",version:"0.1.0"});
server.registerTool("check_document", {
  description:"실습 폴더 안의 UTF-8 텍스트에서 기계적 표기 후보를 찾습니다. 파일을 수정하지 않습니다.",
  inputSchema:{relative_path:z.string().describe("예: sample_contract.txt")},
  annotations:{readOnlyHint:true,destructiveHint:false,openWorldHint:false}
}, async ({relative_path}) => {
  const target = await safePath(relative_path);
  const source = await fs.readFile(target,"utf8");
  return {content:[{type:"text",text:JSON.stringify({file:path.relative(allowedRootReal,target),findings:inspect(source)},null,2)}]};
});
await server.connect(new StdioServerTransport());
