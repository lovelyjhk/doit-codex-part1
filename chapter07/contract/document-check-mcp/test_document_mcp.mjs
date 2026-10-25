import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client({ name: "doit-document-check-test", version: "0.1.0" });
const transport = new StdioClientTransport({ command: process.execPath, args: ["server.mjs"] });

function sanitizeMessage(value) {
  return String(value).replace(/C:\\Users\\[^']+\\/gi, "<실습 폴더>\\");
}

async function captureError(relativePath) {
  try {
    const response = await client.callTool({ name: "check_document", arguments: { relative_path: relativePath } });
    if (response.isError === true) {
      const message = response.content?.map((item) => item.text || "").join(" ") || "MCP 오류 응답";
      return { relative_path: relativePath, rejected: true, message: sanitizeMessage(message) };
    }
    return { relative_path: relativePath, rejected: false, message: "예상과 달리 허용되었습니다." };
  } catch (error) {
    return { relative_path: relativePath, rejected: true, message: sanitizeMessage(error.message || error) };
  }
}

await client.connect(transport);
const tools = await client.listTools();
const normal = await client.callTool({
  name: "check_document",
  arguments: { relative_path: "sample_contract.txt" },
});
const missing = await captureError("missing_document.txt");
const traversal = await captureError("../outside.txt");
const outsideDir = await fs.mkdtemp(path.join(os.tmpdir(), "doit-mcp-outside-"));
const outsideFile = path.join(outsideDir, "outside.txt");
const linkName = `link-escape-${process.pid}`;
const linkPath = path.resolve("..", linkName);
let linkEscape;
try {
  await fs.writeFile(outsideFile, "실습 폴더 밖 가상 파일", "utf8");
  await fs.symlink(outsideDir, linkPath, process.platform === "win32" ? "junction" : "dir");
  linkEscape = await captureError(`${linkName}/outside.txt`);
} catch (error) {
  linkEscape = { relative_path: `${linkName}/outside.txt`, skipped: true, message: `링크·정션 생성 불가: ${error.code || error.message}` };
} finally {
  await fs.unlink(linkPath).catch(() => {});
  await fs.rm(outsideDir, { recursive: true, force: true });
}
const result = {
  checked_at: new Date().toISOString(),
  node_version: process.version,
  tool_names: tools.tools.map((tool) => tool.name),
  normal_case: normal,
  missing_case: missing,
  traversal_case: traversal,
  link_escape_case: linkEscape,
  pass:
    tools.tools.some((tool) => tool.name === "check_document") &&
    missing.rejected === true &&
    traversal.rejected === true &&
    (linkEscape.rejected === true || linkEscape.skipped === true),
};
await fs.writeFile("mcp_test_result.json", JSON.stringify(result, null, 2), "utf8");
await client.close();
console.log(JSON.stringify(result, null, 2));
