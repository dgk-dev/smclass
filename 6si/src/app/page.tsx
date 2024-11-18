import { ContentCard } from "@/components/content/ContentCard";
import { Suspense } from "react";
import { SectionContent } from "@/components/content/SectionContent";

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-b from-brand-50 to-white">
        <div className="container mx-auto px-4 py-12 sm:py-16">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
              대한민국의 모든 콘텐츠를{" "}
              <span className="text-brand-600">한눈에</span>
            </h1>
            <p className="text-lg text-gray-600">
              뉴스, 커뮤니티, 핫딜까지 - 지난 6시간 인기 콘텐츠를 실시간으로 확인하세요.
            </p>
            <p className="text-lg text-gray-600">
              음란글, 정치글, 혐오글 등은 자체 AI 기술을 통해 필터링 됩니다. 
            </p>
          </div>
        </div>
      </section>

      {/* Main Content */}
      <div className="container mx-auto px-4 py-8">
        <div className="flex flex-nowrap gap-8 overflow-x-auto pb-4 scrollbar-hide">
          {/* News Section */}
          <section className="flex-shrink-0 w-[400px]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-blue-500 rounded-full"></span>
                실시간 인기 뉴스
              </h2>
              <a
                href="/section/news"
                className="text-sm text-brand-600 hover:text-brand-700 font-medium transition-colors"
              >
                더보기
              </a>
            </div>
            <Suspense fallback={<div className="animate-pulse">Loading...</div>}>
              <SectionContent category="news" limit={10} />
            </Suspense>
          </section>

          {/* Community Section */}
          <section className="flex-shrink-0 w-[400px]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-green-500 rounded-full"></span>
                인기 커뮤니티 글
              </h2>
              <a
                href="/section/community"
                className="text-sm text-brand-600 hover:text-brand-700 font-medium transition-colors"
              >
                더보기
              </a>
            </div>
            <Suspense fallback={<div className="animate-pulse">Loading...</div>}>
              <SectionContent category="community" limit={10} />
            </Suspense>
          </section>

          {/* Deals Section */}
          <section className="flex-shrink-0 w-[400px]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-red-500 rounded-full"></span>
                오늘의 핫딜
              </h2>
              <a
                href="/section/deals"
                className="text-sm text-brand-600 hover:text-brand-700 font-medium transition-colors"
              >
                더보기
              </a>
            </div>
            <Suspense fallback={<div className="animate-pulse">Loading...</div>}>
              <SectionContent category="deals" limit={10} />
            </Suspense>
          </section>
        </div>
      </div>
    </main>
  );
}
