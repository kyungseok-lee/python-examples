"use client";

import Link from "next/link";
import { useAppState } from "@/contexts/AppContext";

export default function DynamicHeader() {
  const { state } = useAppState();

  return (
    <div className="header">
      <h1 className="main-title">
        <Link href="/">{state.title}</Link>
      </h1>
    </div>
  );
}
