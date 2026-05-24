"use client";

import { useAppStore } from "@/store/app-store";
import { cn } from "@/lib/utils";
import { MessageSquare, Settings, Plus, LayoutPanelLeft, Trash2 } from "lucide-react";
import { motion } from "framer-motion";

import { SettingsDialog } from "@/components/settings/settings-dialog";
import { useState, useEffect } from "react";

export function Sidebar() {
  const { 
    sidebarOpen, 
    toggleSidebar, 
    chats, 
    activeChatId, 
    setActiveChatId, 
    createChat, 
    deleteChat 
  } = useAppStore();
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return <div className="w-[260px] h-full bg-card border-r border-border shrink-0" />;
  }

  return (
    <>
      <motion.div
        initial={{ width: 260 }}
        animate={{ width: sidebarOpen ? 260 : 0, opacity: sidebarOpen ? 1 : 0 }}
        className={cn(
          "h-full bg-card border-r border-border flex flex-col transition-all overflow-hidden whitespace-nowrap",
          !sidebarOpen && "border-none"
        )}
      >
        <div className="p-4 flex items-center justify-between border-b border-border/50">
          <h2 className="font-semibold text-sm tracking-wide">Workspace</h2>
          <button onClick={toggleSidebar} className="p-1 hover:bg-muted rounded-md transition-colors">
            <LayoutPanelLeft className="w-4 h-4 text-muted-foreground hover:text-foreground" />
          </button>
        </div>

        <div className="p-3">
          <button 
            onClick={() => createChat()}
            className="w-full flex items-center gap-2 px-3 py-2 bg-primary/10 text-primary rounded-md text-sm font-medium hover:bg-primary/20 transition-colors"
          >
            <Plus className="w-4 h-4" />
            New Chat
          </button>
        </div>

        <div className="flex-1 overflow-y-auto px-3 py-2 space-y-1 scrollbar-thin scrollbar-thumb-muted">
          <div className="text-xs font-semibold text-muted-foreground px-3 py-2 uppercase tracking-wider">
            Recent Chats
          </div>
          {chats.length === 0 ? (
            <div className="text-xs text-muted-foreground px-3 py-2 italic">
              No chats yet
            </div>
          ) : (
            chats.map((chat) => (
              <div
                key={chat.id}
                onClick={() => setActiveChatId(chat.id)}
                className={cn(
                  "group relative w-full flex items-center gap-2 px-3 py-2 text-sm rounded-md transition-colors text-left cursor-pointer select-none",
                  chat.id === activeChatId
                    ? "bg-primary/15 text-primary font-medium"
                    : "text-muted-foreground hover:bg-muted hover:text-foreground"
                )}
              >
                <MessageSquare className="w-4 h-4 shrink-0 text-muted-foreground/70 group-hover:text-foreground/70" />
                <span className="truncate pr-6 font-medium">{chat.title}</span>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    deleteChat(chat.id);
                  }}
                  className="absolute right-2 opacity-0 group-hover:opacity-100 p-1 hover:bg-destructive/20 text-muted-foreground hover:text-destructive rounded transition-all"
                  title="Delete chat"
                >
                  <Trash2 className="w-3.5 h-3.5" />
                </button>
              </div>
            ))
          )}
        </div>

        <div className="p-3 border-t border-border/50">
          <button onClick={() => setSettingsOpen(true)} className="w-full flex items-center gap-2 px-3 py-2 text-sm text-muted-foreground hover:bg-muted hover:text-foreground rounded-md transition-colors text-left">
            <Settings className="w-4 h-4 shrink-0" />
            Settings
          </button>
        </div>
      </motion.div>
      <SettingsDialog open={settingsOpen} onClose={() => setSettingsOpen(false)} />
    </>
  );
}

