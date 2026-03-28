"use client";

import Image from "next/image";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Landmark, Compass, Target } from "lucide-react";
import { useLanguage } from "@/components/LanguageContext";
import { translations } from "@/lib/translations";
import clsx from "clsx";

export default function AboutPage() {
  const { lang, isRTL } = useLanguage();
  const t = translations[lang];

  return (
    <div className="bg-offwhite flex flex-col min-h-screen">
      {/* 1. HERO SECTION */}
      <section className="relative w-full h-[60vh] min-h-[400px] flex items-center overflow-hidden bg-forest">
        <div className="absolute inset-0 z-0">
          <Image
            src="/images/home_hero.png"
            alt="Bulker ship representing global reach"
            fill
            priority
            className="object-cover object-[98%_center] md:object-center opacity-40 hover:opacity-60 transition-opacity duration-1000"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6 flex items-center gap-3">
              <Landmark className="w-6 h-6 text-gold" />
              <span className="text-gold font-serif italic tracking-wide">
                {t.about.hero.profile}
              </span>
            </StaggerItem>
            <StaggerItem direction="up" className="mb-6">
              <h1 className={clsx("text-5xl md:text-7xl lg:text-8xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.85]", isRTL && "font-arabic")}>
                {lang === 'ar' ? <>من <br /> نحن</> : <>About <br /> Us</>}
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className="text-offwhite/90 text-base md:text-lg font-normal leading-relaxed max-w-xl text-balance">
                {t.about.hero.desc}
              </p>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 2. TEXT CONTENT & CORPORATE STATEMENTS */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite overflow-hidden">
        <div className="container mx-auto px-4 md:px-8">

          <div className="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-16 lg:gap-24">

            {/* Left Column: Who We Are */}
            <div className="md:col-span-7 lg:col-span-8">
              <AnimatedSection direction="up" className="mb-12">
                <h2 className={clsx("text-4xl md:text-6xl font-serif font-bold text-forest uppercase tracking-tighter mb-8", isRTL && "font-arabic")}>
                  {lang === 'ar' ? <>من <span className="text-gold italic font-normal font-sans">نحن.</span></> : <>Who We <span className="text-gold italic font-normal">Are.</span></>}
                </h2>
                <div className={clsx("space-y-6 text-forest/90 font-normal text-base md:text-lg leading-relaxed text-balance", isRTL && "text-start")}>
                  <p>
                    <strong className={clsx("font-bold text-forest", isRTL && "font-arabic")}>
                      {lang === 'ar' ? "بلاك روك آند يلو ساندز إنترناشيونال" : "Black Rock And Yellow Sands International"}
                    </strong> {lang === 'ar' ? "هي مورد بالجملة رائد يعمل في جوهر التجارة العالمية. نحن نقدم مواد ذات جودة استثنائية، تلبي عتبات النقاء الصارمة ومعايير ISO، مع مراعاة معايير الانبعاثات في منتجاتنا." : "is a premier wholesale supplier operating at the nexus of global trade. We deliver materials of exceptional quality, meeting strict purity thresholds and ISO standards, concerning emissions standards in our products."}
                  </p>
                  <p>
                    {t.about.content.p2}
                  </p>
                  <p>
                    {t.about.content.p3}
                  </p>
                  <p>
                    {t.about.content.p4}
                  </p>
                </div>
              </AnimatedSection>
            </div>

            {/* Right Column: Vision & Mission */}
            <div className={clsx("md:col-span-5 lg:col-span-4 flex flex-col gap-12 border-t md:border-t-0 border-forest/10 pt-12 md:pt-0", isRTL ? "md:border-r md:pr-12 lg:pr-16" : "md:border-l md:pl-12 lg:pl-16")}>

              <AnimatedSection direction={isRTL ? "right" : "left"} delay={0.2} className="relative">
                <Compass className="w-8 h-8 text-gold mb-6" />
                <h3 className={clsx("text-2xl font-serif font-bold text-forest mb-4", isRTL && "text-start font-arabic")}>
                  {t.about.content.visionTitle}
                </h3>
                <p className={clsx("text-forest/80 font-normal text-base leading-relaxed text-balance", isRTL && "text-start")}>
                  {t.about.content.visionDesc}
                </p>
              </AnimatedSection>

              <div className="w-12 h-px bg-forest/10" />

              <AnimatedSection direction={isRTL ? "right" : "left"} delay={0.4} className="relative">
                <Target className="w-8 h-8 text-gold mb-6" />
                <h3 className={clsx("text-2xl font-serif font-bold text-forest mb-4", isRTL && "text-start font-arabic")}>
                  {t.about.content.missionTitle}
                </h3>
                <p className={clsx("text-forest/80 font-normal text-base leading-relaxed text-balance", isRTL && "text-start")}>
                  {t.about.content.missionDesc}
                </p>
              </AnimatedSection>
            </div>
          </div>

        </div>
      </section>
    </div>
  );
}
