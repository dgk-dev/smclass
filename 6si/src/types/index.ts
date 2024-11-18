import { Category } from '@/lib/constants';

export interface Content {
  id: string;
  title: string;
  thumbnail: string;
  source: string;
  category: Category;
  url: string;
  timestamp: string;
  likes: number;
  bookmarks: number;
}

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
}
