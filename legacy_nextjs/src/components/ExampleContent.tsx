"use client";

import { useState, useEffect, useRef } from "react";

interface CodeSection {
  explanation: string;
  code: string;
}

interface ExampleContentProps {
  title: string;
  description: string;
  codeSections: CodeSection[];
  output?: string;
  fullCode: string;
}

export default function ExampleContent({
  title,
  description,
  codeSections,
  output,
  fullCode,
}: ExampleContentProps) {
  const [copied, setCopied] = useState(false);
  const codeRefs = useRef<(HTMLElement | null)[]>([]);

  useEffect(() => {
    const loadPrism = async () => {
      if (typeof window !== "undefined") {
        try {
          const Prism = (await import("prismjs")).default;
          await import("prismjs/components/prism-python.js");

          codeRefs.current.forEach((ref) => {
            if (ref) {
              Prism.highlightElement(ref);
            }
          });
        } catch (error) {
          console.log("Prism.js 로딩 실패, 기본 텍스트로 표시");
        }
      }
    };
    loadPrism();
  }, [codeSections]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(fullCode);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error("복사 실패:", err);
    }
  };

  const handleRunCode = () => {
    const encodedCode = encodeURIComponent(fullCode);
    window.open(
      `https://python-playground.netlify.app/?code=${encodedCode}`,
      "_blank"
    );
  };

  return (
    <div className="example-content">
      <div className="example-header">
        <p className="example-description">{description}</p>
        <div className="example-actions">
          <button
            onClick={handleRunCode}
            className="action-button run-button"
            title="온라인에서 실행"
          >
            ▶️
          </button>
          <button
            onClick={handleCopy}
            className="action-button copy-button"
            title="전체 코드 복사"
          >
            {copied ? "✓" : "📋"}
          </button>
        </div>
      </div>

      <div className="example-table">
        {codeSections.map((section, index) => (
          <div key={index} className="example-row">
            <div className="explanation-cell">
              {section.explanation && <p>{section.explanation}</p>}
            </div>
            <div className="code-cell">
              <pre>
                <code
                  ref={(el) => {
                    codeRefs.current[index] = el;
                  }}
                  className="language-python"
                >
                  {section.code}
                </code>
              </pre>
            </div>
          </div>
        ))}
      </div>

      {output && (
        <div className="example-table">
          <div className="example-row">
            <div className="explanation-cell"></div>
            <div className="output-cell">
              <pre className="output-content">
                $ python example.py{"\n"}
                {output}
              </pre>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
