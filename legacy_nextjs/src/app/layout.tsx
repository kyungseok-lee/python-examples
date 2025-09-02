import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";
import Link from "next/link";
import type { Metadata } from "next";
import "@/app/globals.css";
import DynamicHeader from "@/components/DynamicHeader";
import FooterText from "@/components/FooterText";
import { AppProvider } from "@/contexts/AppContext";

export const metadata: Metadata = {
  title: "Python by Example",
  description:
    "Python by Example is a hands-on introduction to Python using annotated example programs. Inspired by Go by Example.",
  keywords: [
    "Python",
    "Python by Example",
    "Go by Example",
    "Programming",
    "Tutorial",
    "Code Examples",
  ],
  openGraph: {
    title: "Python by Example",
    description:
      "A hands-on introduction to Python using annotated example programs.",
    url: "https://python-by-example.vercel.app",
    siteName: "Python by Example",
    locale: "en_US",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: `{
          "@context": "https://schema.org",
          "@type": "SoftwareApplication",
          "name": "Python by Example",
          "url": "https://python-by-example.vercel.app",
          "applicationCategory": "EducationalApplication",
          "operatingSystem": "All",
          "description": "A hands-on introduction to Python using annotated example programs.",
          "license": "https://github.com/kyungseok-lee/python-by-example/blob/main/LICENSE"
        }`,
          }}
        />
      </head>
      <body>
        <AppProvider>
          <div className="main-container">
            <div className="header">
              <DynamicHeader />
            </div>
            <div className="body">{children}</div>
            <div className="footer">
              <FooterText />
            </div>
          </div>
        </AppProvider>
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}
