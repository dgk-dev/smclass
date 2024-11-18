import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { AuthProvider } from "@/contexts/auth";
import { Header } from "@/components/layout/Header";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "6si.kr - 뉴스, 커뮤니티, 할인정보",
  description: "6시간마다 업데이트되는 뉴스, 커뮤니티, 할인정보 모음",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko" className={`${geistSans.variable} ${geistMono.variable}`} suppressHydrationWarning>
      <body className="min-h-screen bg-white dark:bg-gray-900" suppressHydrationWarning>
        <AuthProvider>
          <Header />
          <main className="flex min-h-screen flex-col">{children}</main>
        </AuthProvider>
      </body>
    </html>
  );
}
