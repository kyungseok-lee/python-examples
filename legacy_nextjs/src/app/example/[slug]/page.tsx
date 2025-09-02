import Link from "next/link";
import { notFound } from "next/navigation";
import { Metadata } from "next";
import { getExampleBySlug, getNavigationForExample } from "@/lib/data";
import ExamplePageClient from "@/components/ExamplePageClient";

interface ExamplePageProps {
  params: {
    slug: string;
  };
}

export async function generateMetadata({
  params,
}: ExamplePageProps): Promise<Metadata> {
  const example = getExampleBySlug(params.slug);

  if (!example) {
    return {
      title: "Python by Example",
    };
  }

  return {
    title: `Python by Example: ${example.title}`,
    description: example.explanation,
  };
}

export default function ExamplePage({ params }: ExamplePageProps) {
  const example = getExampleBySlug(params.slug);

  if (!example) {
    notFound();
  }

  const navigation = getNavigationForExample(params.slug);

  return <ExamplePageClient example={example} navigation={navigation} />;
}
