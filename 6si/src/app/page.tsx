import { CATEGORIES } from '@/lib/constants';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-section">
      {/* Hero Section */}
      <section className="mb-section text-center">
        <h1 className="text-4xl font-bold mb-4">
          6시간마다 업데이트되는<br />
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-news via-community to-deals">
            최신 소식과 정보
          </span>
        </h1>
        <p className="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
          뉴스, 커뮤니티, 할인정보를 한눈에 확인하세요
        </p>
      </section>

      {/* News Section */}
      <section className="mb-section animate-slide-up">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-news">{CATEGORIES.news}</h2>
          <Link 
            href="/section/news"
            className="group flex items-center gap-2 text-sm text-gray-600 hover:text-news transition-colors"
          >
            더보기
            <span className="transition-transform group-hover:translate-x-1">→</span>
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>

      {/* Community Section */}
      <section className="mb-section animate-slide-up [animation-delay:200ms]">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-community">{CATEGORIES.community}</h2>
          <Link 
            href="/section/community"
            className="group flex items-center gap-2 text-sm text-gray-600 hover:text-community transition-colors"
          >
            더보기
            <span className="transition-transform group-hover:translate-x-1">→</span>
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>

      {/* Deals Section */}
      <section className="mb-section animate-slide-up [animation-delay:400ms]">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-deals">{CATEGORIES.deals}</h2>
          <Link 
            href="/section/deals"
            className="group flex items-center gap-2 text-sm text-gray-600 hover:text-deals transition-colors"
          >
            더보기
            <span className="transition-transform group-hover:translate-x-1">→</span>
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>
    </div>
  );
}
