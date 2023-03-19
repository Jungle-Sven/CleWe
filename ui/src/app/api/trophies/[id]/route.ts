import { NextRequest } from "next/server";

export async function PUT(request: NextRequest) {
  const apiPath = new URL(request.nextUrl).pathname;
  const requestBody = await request.json();
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${apiPath}`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "PUT",
    body: JSON.stringify({
      tx_hash: requestBody["tx_hash"],
    }),
  });
  return res;
}
