import { NextRequest } from "next/server";

export async function PATCH(request: NextRequest) {
  const apiPath = new URL(request.nextUrl).pathname;
  const requestBody = await request.json();
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${apiPath}`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "PATCH",
    body: JSON.stringify({
      user_id: Number(requestBody["user_id"]),
    }),
  });
  return res;
}
