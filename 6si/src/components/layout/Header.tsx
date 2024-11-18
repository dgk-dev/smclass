"use client";

import Link from 'next/link';
import { SearchBar } from '../shared/SearchBar';
import { UserMenu } from '../shared/UserMenu';
import { CATEGORIES } from '@/lib/constants';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-white/95 dark:bg-gray-900/95">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="text-2xl font-bold">
          6si.kr
        </Link>
        
        <nav className="hidden md:flex items-center space-x-6">
          <Link 
            href="/section/news" 
            className="text-[#0066FF] hover:text-[#0066FF]/80"
          >
            {CATEGORIES.news}
          </Link>
          <Link 
            href="/section/community" 
            className="text-[#00CC00] hover:text-[#00CC00]/80"
          >
            {CATEGORIES.community}
          </Link>
          <Link 
            href="/section/deals" 
            className="text-[#FF0000] hover:text-[#FF0000]/80"
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
