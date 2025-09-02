"use client";

import Link from "next/link";

export default function FooterText() {
  return (
    <div className="footer-content">
      <p>
        Inspired by{" "}
        <Link
          href="https://gobyexample.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Go by Example
        </Link>
        <span className="separator">|</span>
        <Link
          href="https://github.com/kyungseok-lee/python-by-example"
          target="_blank"
          rel="noopener noreferrer"
        >
          Source
        </Link>
        <span className="separator">|</span>
        <Link
          href="https://github.com/kyungseok-lee/python-by-example/blob/main/LICENSE"
          target="_blank"
          rel="noopener noreferrer"
        >
          License
        </Link>
      </p>
    </div>
  );
}
