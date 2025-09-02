"use client";

import Link from "next/link";
import CodeBlock from "@/components/CodeBlock";
import PageTitle from "@/components/PageTitle";
import { Example } from "@/lib/data";

interface ExamplePageClientProps {
  example: Example;
  navigation: {
    prev: Example | null;
    next: Example | null;
  };
}

export default function ExamplePageClient({
  example,
  navigation,
}: ExamplePageClientProps) {
  return (
    <>
      <PageTitle title={`Python by Example: ${example.title}`} />

      <p className="example-description">{example.description}</p>

      <CodeBlock code={example.code} output={example.output} />

      <div className="example-explanation">
        <p>{example.explanation}</p>
      </div>

      <div className="example-nav">
        <Link href="/" className="example-nav-index">
          Index
        </Link>

        <div className="example-nav-examples">
          {navigation.prev && (
            <Link
              href={`/example/${navigation.prev.slug}`}
              className="example-nav-prev"
            >
              {navigation.prev.title}
            </Link>
          )}
          {navigation.prev && navigation.next && (
            <span className="example-nav-separator">|</span>
          )}
          {navigation.next && (
            <Link
              href={`/example/${navigation.next.slug}`}
              className="example-nav-next"
            >
              {navigation.next.title}
            </Link>
          )}
        </div>
      </div>
    </>
  );
}
