"use client";

import { useState, useEffect, useRef } from "react";

interface CodeBlockProps {
  code: string;
  output?: string;
  title?: string;
  showCopy?: boolean;
}

export default function CodeBlock({
  code,
  output,
  title,
  showCopy = true,
}: CodeBlockProps) {
  const [copied, setCopied] = useState(false);
  const codeRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const loadPrism = async () => {
      if (typeof window !== "undefined" && codeRef.current) {
        try {
          const Prism = (await import("prismjs")).default;
          // Python 언어 지원 로드
          await import("prismjs/components/prism-python.js");
          Prism.highlightElement(codeRef.current);
        } catch (error) {
          console.log("Prism.js load failed, showing plain text");
        }
      }
    };
    loadPrism();
  }, [code]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error("Copy failed:", err);
    }
  };

  const handleRunCode = () => {
    const encodedCode = encodeURIComponent(code);
    window.open(
      `https://python-playground.netlify.app/?code=${encodedCode}`,
      "_blank"
    );
  };

  return (
    <>
      {/* 코드 블록 */}
      <div className="code-block">
        {title && (
          <div className="code-header">
            <div className="code-title">{title}</div>
            {showCopy && (
              <button
                onClick={handleCopy}
                className={`copy-button${copied ? " copied" : ""}`}
                title="Copy"
              >
                <span role="img" aria-label="copy">
                  📋
                </span>
                {copied ? "Copied!" : "Copy"}
              </button>
            )}
          </div>
        )}
        <div className="code-content">
          <pre>
            <code ref={codeRef} className="language-python">
              {code}
            </code>
          </pre>
        </div>
        <div className="code-actions">
          {showCopy && (
            <button
              onClick={handleCopy}
              className={`copy-button${copied ? " copied" : ""}`}
              title="Copy"
            >
              <span role="img" aria-label="copy">
                📋
              </span>
              {copied ? " Copied!" : " Copy"}
            </button>
          )}
          <button onClick={handleRunCode} className="run-button" title="Run">
            <span role="img" aria-label="run">
              ▶️
            </span>
            {" Run"}
          </button>
        </div>
      </div>

      {/* 출력 결과 */}
      {output && (
        <div className="output-block">
          Output:
          <pre>{output}</pre>
        </div>
      )}
    </>
  );
}
