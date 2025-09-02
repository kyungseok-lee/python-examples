// If you get a TS error, ensure you have a src/types/json.d.ts with: declare module '*.json';
import examplesData from "@/data/examples.json";

export interface Example {
  id: number;
  title: string;
  slug: string;
  description: string;
  code: string;
  explanation: string;
  output: string;
  order: number;
}

export const getExamples = (): Example[] => {
  return (examplesData as Example[]).sort(
    (a: Example, b: Example) => a.order - b.order
  );
};

export const getExampleBySlug = (slug: string): Example | undefined => {
  return (examplesData as Example[]).find(
    (example: Example) => example.slug === slug
  );
};

export const getNavigationForExample = (
  slug: string
): { prev: Example | null; next: Example | null } => {
  const allExamples = getExamples();
  const currentIndex = allExamples.findIndex(
    (example) => example.slug === slug
  );

  return {
    prev: currentIndex > 0 ? allExamples[currentIndex - 1] : null,
    next:
      currentIndex < allExamples.length - 1
        ? allExamples[currentIndex + 1]
        : null,
  };
};
