import { Category } from '@/lib/constants';
import { Database } from '@/lib/supabase/database.types';

export type Content = Database['public']['Tables']['contents']['Row'];

export interface User {
  id: string;
  email: string;
  bookmarks: string[];
  likes: string[];
  readItems: string[];
}

export interface ContentCard {
  thumbnail: string;
  title: string;
  source: string;
  timestamp: string;
  isNew?: boolean;
  category: Category;
  url: string;
  likes?: number;
  bookmarks?: number;
}
