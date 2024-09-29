import type { Metadata } from "next";
import { Lexend_Deca } from "next/font/google";
import "./globals.css";
import "@fortawesome/fontawesome-svg-core/styles.css";
import { config } from "@fortawesome/fontawesome-svg-core";

config.autoAddCss = false;

const font = Lexend_Deca({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "educAItion",
  description: "AI powerd education app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${font.className} antialiased bg-black py-12 px-4 bg-[radial-gradient(100%_100%_at_0%_0%,rgba(50,1,71,1)_13%,#000_93%)]`}
      >
        {children}
      </body>
    </html>
  );
}
