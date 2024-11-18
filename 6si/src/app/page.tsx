import { CATEGORIES } from '@/lib/constants';
import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-surface-50">
      {/* Hero Section */}
      <div className="relative overflow-hidden border-b border-surface-200">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#4F46E5_0%,#10B981_50%,#DC2626_100%)] opacity-5" />
        <div className="container mx-auto px-4 py-section relative">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-5xl font-bold tracking-tight mb-6">
              6시간마다 업데이트되는{' '}
              <span className="relative">
                <span className="relative z-10 bg-gradient-to-r from-brand-700 to-brand-900 bg-clip-text text-transparent">
                  최신 소식과 정보
                </span>
                <span className="absolute -bottom-2 left-0 right-0 h-3 bg-brand-100 -rotate-1" />
              </span>
            </h1>
            <p className="text-lg text-surface-600 mb-8">
              뉴스, 커뮤니티, 할인정보를 한눈에 확인하세요
            </p>
            <div className="inline-flex items-center gap-2 text-sm text-surface-500">
              <span className="inline-block w-2 h-2 rounded-full bg-accent-green animate-pulse" />
              실시간 업데이트 중
            </div>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 py-section">
        {/* News Section */}
        <section className="mb-section animate-slide-up">
          <div className="flex justify-between items-center mb-8">
            <div className="space-y-1">
              <h2 className="text-2xl font-bold text-surface-900">
                {CATEGORIES.news}
              </h2>
              <p className="text-surface-500">오늘의 주요 뉴스를 확인하세요</p>
            </div>
            <Link 
              href="/section/news"
              className="group inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-surface-100 hover:bg-surface-200 text-surface-900 transition-colors"
            >
              더보기
              <span className="transition-transform group-hover:translate-x-0.5">→</span>
            </Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Content cards will be added here */}
          </div>
        </section>

        {/* Community Section */}
        <section className="mb-section animate-slide-up [animation-delay:100ms]">
          <div className="flex justify-between items-center mb-8">
            <div className="space-y-1">
              <h2 className="text-2xl font-bold text-surface-900">
                {CATEGORIES.community}
              </h2>
              <p className="text-surface-500">실시간 인기 게시글을 확인하세요</p>
            </div>
            <Link 
              href="/section/community"
              className="group inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-surface-100 hover:bg-surface-200 text-surface-900 transition-colors"
            >
              더보기
              <span className="transition-transform group-hover:translate-x-0.5">→</span>
            </Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Content cards will be added here */}
          </div>
        </section>

        {/* Deals Section */}
        <section className="mb-section animate-slide-up [animation-delay:200ms]">
          <div className="flex justify-between items-center mb-8">
            <div className="space-y-1">
              <h2 className="text-2xl font-bold text-surface-900">
                {CATEGORIES.deals}
              </h2>
              <p className="text-surface-500">오늘의 특가 상품을 확인하세요</p>
            </div>
            <Link 
              href="/section/deals"
              className="group inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-surface-100 hover:bg-surface-200 text-surface-900 transition-colors"
            >
              더보기
              <span className="transition-transform group-hover:translate-x-0.5">→</span>
            </Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Content cards will be added here */}
          </div>
        </section>
      </div>
    </main>
  );
}
