import { NextRequest, NextResponse } from "next/server";

export async function PUT(request: NextRequest) {
  console.log("PUT trophie called", request);
  return new NextResponse("PUT trophy echo", {
    status: 200,
  });
}
