"use client";

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/contexts/auth';
import { createClient } from '@/lib/supabase/client';
import { User, LogOut, Bookmark } from 'lucide-react';

export function UserMenu() {
  const [isOpen, setIsOpen] = useState(false);
  const { user } = useAuth();
  const router = useRouter();
  const supabase = createClient();

  const handleLogout = async () => {
    await supabase.auth.signOut();
    router.refresh();
  };

  const handleLogin = () => {
    router.push('/auth/login');
  };

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center justify-center w-10 h-10 rounded-full bg-gray-50 text-gray-500 hover:bg-gray-100 hover:text-brand-500 transition-colors"
      >
        <User className="w-5 h-5" />
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-56 rounded-lg border border-gray-100 bg-white shadow-lg">
          <div className="py-1">
            {user ? (
              <>
                <div className="px-4 py-3 text-sm text-gray-900 border-b border-gray-100">
                  <p className="font-medium truncate">{user.email}</p>
                </div>
                <Link
                  href="/bookmarks"
                  className="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-500 transition-colors"
                >
                  <Bookmark className="w-4 h-4 mr-2" />
                  북마크
                </Link>
                <button
                  className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-500 transition-colors"
                  onClick={handleLogout}
                >
                  <LogOut className="w-4 h-4 mr-2" />
                  로그아웃
                </button>
              </>
            ) : (
              <button
                className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-500 transition-colors"
                onClick={handleLogin}
              >
                <User className="w-4 h-4 mr-2" />
                로그인
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
