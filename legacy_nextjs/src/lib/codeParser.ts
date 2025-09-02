interface CodeSection {
  explanation: string;
  code: string;
}

export function parseCodeSections(
  code: string,
  explanation: string
): CodeSection[] {
  // 코드를 라인별로 분할
  const lines = code.split("\n");
  const sections: CodeSection[] = [];
  let currentCode = "";
  let currentExplanation = "";

  // 주석이 있는 라인을 기준으로 섹션 나누기
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (line.trim().startsWith("#") && line.trim().length > 1) {
      // 이전 섹션을 저장
      if (currentCode.trim()) {
        sections.push({
          explanation: currentExplanation,
          code: currentCode.trim(),
        });
      }

      // 새 섹션 시작
      currentExplanation = line.replace(/^#\s*/, "").trim();
      currentCode = "";
    } else if (line.trim()) {
      // 코드 라인 추가
      currentCode += (currentCode ? "\n" : "") + line;
    }
  }

  // 마지막 섹션 추가
  if (currentCode.trim()) {
    sections.push({
      explanation: currentExplanation,
      code: currentCode.trim(),
    });
  }

  // 섹션이 없으면 전체 코드와 설명을 하나의 섹션으로
  if (sections.length === 0) {
    return [
      {
        explanation: explanation,
        code: code,
      },
    ];
  }

  return sections;
}

export function getFullCode(sections: CodeSection[]): string {
  return sections.map((section) => section.code).join("\n\n");
}
