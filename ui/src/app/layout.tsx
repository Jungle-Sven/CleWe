import "./globals.css";

export const metadata = {
  title: "Landing",
  description: "Welcome to CleWe - Web3 education made as game-engaing",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
