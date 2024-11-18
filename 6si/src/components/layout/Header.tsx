"use client";

import Link from 'next/link';
import { SearchBar } from '../shared/SearchBar';
import { UserMenu } from '../shared/UserMenu';
import { CATEGORIES } from '@/lib/constants';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-gray-100 bg-white/80 backdrop-blur-md">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="text-2xl font-bold text-gray-900">
          6si.kr
        </Link>
        
        <nav className="hidden md:flex items-center space-x-8">
          <Link 
            href="/section/news" 
            className="text-gray-600 hover:text-brand-600 transition-colors font-medium"
          >
            {CATEGORIES.news}
          </Link>
          <Link 
            href="/section/community" 
            className="text-gray-600 hover:text-brand-600 transition-colors font-medium"
          >
            {CATEGORIES.community}
          </Link>
          <Link 
            href="/section/deals" 
            className="text-gray-600 hover:text-brand-600 transition-colors font-medium"
          >
            {CATEGORIES.deals}
          </Link>
        </nav>

        <div className="flex items-center space-x-4">
          <SearchBar />
          <UserMenu />
        </div>
      </div>
    </header>
  );
}
