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

export interface ContentCardProps extends Pick<Content, 'thumbnail' | 'title' | 'source' | 'timestamp' | 'category' | 'url' | 'likes' | 'bookmarks'> {
  isNew?: boolean;
  isLiked?: boolean;
  isBookmarked?: boolean;
  onLike?: () => void;
  onBookmark?: () => void;
  onClick?: () => void;
}
