export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      contents: {
        Row: {
          id: string
          title: string
          thumbnail: string
          source: string
          category: 'news' | 'community' | 'deals'
          url: string
          timestamp: string
          likes: number
          bookmarks: number
          created_at: string
        }
        Insert: {
          id?: string
          title: string
          thumbnail: string
          source: string
          category: 'news' | 'community' | 'deals'
          url: string
          timestamp?: string
          likes?: number
          bookmarks?: number
          created_at?: string
        }
        Update: {
          id?: string
          title?: string
          thumbnail?: string
          source?: string
          category?: 'news' | 'community' | 'deals'
          url?: string
          timestamp?: string
          likes?: number
          bookmarks?: number
          created_at?: string
        }
      }
      user_interactions: {
        Row: {
          id: string
          user_id: string
          content_id: string
          type: 'bookmark' | 'like' | 'read'
          created_at: string
        }
        Insert: {
          id?: string
          user_id: string
          content_id: string
          type: 'bookmark' | 'like' | 'read'
          created_at?: string
        }
        Update: {
          id?: string
          user_id?: string
          content_id?: string
          type?: 'bookmark' | 'like' | 'read'
          created_at?: string
        }
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      [_ in never]: never
    }
  }
}
