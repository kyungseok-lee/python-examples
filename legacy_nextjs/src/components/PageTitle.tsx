"use client";

import { useEffect } from "react";
import { useAppState } from "@/contexts/AppContext";

interface PageTitleProps {
  title: string;
}

export default function PageTitle({ title }: PageTitleProps) {
  const { setTitle, resetTitle } = useAppState();

  useEffect(() => {
    setTitle(title);

    return () => {
      resetTitle();
    };
  }, [title]);

  return null;
}
