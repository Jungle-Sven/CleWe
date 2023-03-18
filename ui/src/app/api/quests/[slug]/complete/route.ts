import { NextRequest } from "next/server";

export async function PATCH(request: NextRequest) {
  const apiPath = new URL(request.nextUrl).pathname;
  const requestBody = await request.json();
  console.log("Request body", requestBody["user_id"]);
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${apiPath}`, {
    method: "PATCH",
    body: JSON.stringify({
      user_id: requestBody["user_id"],
    }),
  });
  return res;
}
