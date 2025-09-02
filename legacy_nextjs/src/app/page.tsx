"use client";

import Link from "next/link";
import { getExamples } from "@/lib/data";

export default function HomePage() {
  const examples = getExamples();

  return (
    <>
      <div className="intro">
        <p>
          <Link href="https://python.org/">Python</Link> is an open source
          programming language designed for simplicity, versatility, and
          readability. Please read the{" "}
          <Link href="https://docs.python.org/3/tutorial/">
            official documentation
          </Link>{" "}
          to learn more.
        </p>
        <p>
          <em>Python by Example</em> is a hands-on introduction to Python using
          annotated example programs. Check out the{" "}
          <Link href="/example/hello-world">first example</Link> or browse the
          full list below.
        </p>
        <p>
          Unless stated otherwise, examples here assume the latest major release
          of Python and may use new language features. Try upgrading to the
          latest version if something isn't working.
        </p>
      </div>
      <ul className="examples-list">
        {examples.map((example) => (
          <li key={example.id}>
            <Link href={`/example/${example.slug}`}>{example.title}</Link>
          </li>
        ))}
      </ul>
    </>
  );
}
