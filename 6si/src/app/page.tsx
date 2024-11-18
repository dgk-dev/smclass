import { ContentCard } from "@/components/content/ContentCard";
import { Suspense } from "react";

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-b from-brand-50 to-white">
        <div className="container mx-auto px-4 py-16 sm:py-24">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-6">
              한국의 모든 콘텐츠를{" "}
              <span className="text-brand-600">한눈에</span>
            </h1>
            <p className="text-lg text-gray-600 mb-8">
              뉴스, 커뮤니티, 핫딜까지 - 모든 인기 콘텐츠를 실시간으로 확인하세요
            </p>
          </div>
        </div>
      </section>

      {/* News Section */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-gray-900">
              실시간 인기 뉴스
            </h2>
            <a
              href="#"
              className="text-brand-600 hover:text-brand-700 font-medium transition-colors"
            >
              더보기
            </a>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Suspense fallback={<div>Loading...</div>}>
              {/* News Cards */}
              <ContentCard
                thumbnail="https://via.placeholder.com/600x314"
                title="삼성전자, 차세대 메모리 반도체 개발 성공"
                source="서울경제"
                timestamp={new Date().toISOString()}
                category="news"
                url="#"
                isNew={true}
                likes={128}
                bookmarks={45}
              />
              {/* Add more news cards */}
            </Suspense>
          </div>
        </div>
      </section>

      {/* Community Section */}
      <section className="py-12 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-gray-900">
              인기 커뮤니티 글
            </h2>
            <a
              href="#"
              className="text-brand-600 hover:text-brand-700 font-medium transition-colors"
            >
              더보기
            </a>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Suspense fallback={<div>Loading...</div>}>
              {/* Community Cards */}
              <ContentCard
                thumbnail="https://via.placeholder.com/600x314"
                title="오늘 서울 날씨 장난 아니네요"
                source="클리앙"
                timestamp={new Date().toISOString()}
                category="community"
                url="#"
                isNew={true}
                likes={256}
                bookmarks={89}
              />
              {/* Add more community cards */}
            </Suspense>
          </div>
        </div>
      </section>

      {/* Deals Section */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-gray-900">
              오늘의 핫딜
            </h2>
            <a
              href="#"
              className="text-brand-600 hover:text-brand-700 font-medium transition-colors"
            >
              더보기
            </a>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Suspense fallback={<div>Loading...</div>}>
              {/* Deals Cards */}
              <ContentCard
                thumbnail="https://via.placeholder.com/600x314"
                title="Apple 에어팟 프로 2세대 특가"
                source="뽐뿌"
                timestamp={new Date().toISOString()}
                category="deals"
                url="#"
                isNew={true}
                likes={512}
                bookmarks={167}
              />
              {/* Add more deals cards */}
            </Suspense>
          </div>
        </div>
      </section>
    </main>
  );
}
