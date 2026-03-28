"use client";

import Image from "next/image";
import Link from "next/link";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Mountain } from "lucide-react";
import { useLanguage } from "@/components/LanguageContext";
import { translations } from "@/lib/translations";
import clsx from "clsx";

export default function SulfurPage() {
  const { lang, isRTL } = useLanguage();
  const t = translations[lang];

  return (
    <div className="bg-offwhite flex flex-col min-h-screen">
      {/* 1. HERO SECTION */}
      <section className="relative w-full h-[70vh] min-h-[500px] flex items-center overflow-hidden bg-forest">
        <div className="absolute inset-0 z-0">
          <Image
            src="/images/sulfur_pile_hero.png"
            alt="Sulfur Pile Hero"
            fill
            priority
            className="object-cover object-center opacity-40 hover:opacity-60 transition-opacity duration-1000"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-forest/10" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6 flex items-center gap-3">
              <Mountain className="w-6 h-6 text-gold" />
              <span className="text-gold font-serif italic tracking-wide">
                {t.sulfur.hero.titleGold}
              </span>
            </StaggerItem>
            <StaggerItem direction="up" className="mb-6">
              <h1 className={clsx("text-5xl md:text-7xl lg:text-8xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.85]", isRTL && "font-arabic")}>
                {lang === 'ar' ? <>تجارة <br /> الكبريت</> : <>Sulfur <br /> Trading</>}
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className={clsx("text-offwhite/80 text-base md:text-lg font-normal leading-relaxed max-w-xl text-balance", isRTL && "text-start")}>
                {t.sulfur.hero.desc}
              </p>
              <Link
                href="/contact"
                className="inline-flex mt-8 px-8 py-3 bg-gold text-forest font-bold tracking-widest text-xs rounded-sm hover:bg-offwhite transition-colors uppercase"
              >
                {t.common.requestAQuote}
              </Link>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 2. OVERVIEW & CAPABILITIES */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite">
        <div className="container mx-auto px-4 md:px-8">
          <AnimatedSection direction="up" className="mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8 text-forest">
            <div className="max-w-2xl">
              <h2 className={clsx("text-3xl md:text-5xl font-serif font-bold uppercase tracking-tighter", isRTL && "font-arabic")}>
                {lang === 'ar' ? <>قوة <span className="text-gold italic font-normal font-sans">خام.</span></> : <>Raw <span className="text-gold italic font-normal">Power.</span></>}
              </h2>
              <p className={clsx("mt-6 text-lg font-normal leading-relaxed text-balance opacity-80", isRTL && "text-start")}>
                {t.sulfur.content.rawPowerDesc}
              </p>
            </div>
          </AnimatedSection>

          {/* Granular Sulfur Split Section */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-16 items-center">
            <AnimatedSection direction="left" className="relative h-[400px] md:h-[600px] rounded-sm overflow-hidden group">
              <Image
                src="/images/granular_sulfur.jpg"
                alt="Granular Sulfur Material"
                fill
                className="object-cover object-center opacity-90 hover:opacity-100 transition-all duration-1000 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/80 via-transparent to-transparent" />
              <div className="absolute bottom-0 left-0 p-8 w-full border-b-4 border-gold">
                <span className="text-gold font-sans font-bold text-xs tracking-widest uppercase mb-2 block">
                  {t.sulfur.content.gradeA}
                </span>
                <h3 className="text-2xl font-serif font-bold text-offwhite">
                  {t.sulfur.content.premiumSulfur}
                </h3>
              </div>
            </AnimatedSection>

            <StaggerContainer className="flex flex-col gap-10">
              <StaggerItem className={clsx("border-forest/10 hover:border-gold transition-colors pt-2 pb-2", isRTL ? "border-r-2 pr-6" : "border-l-2 pl-6")}>
                <h3 className={clsx("text-xl font-serif font-bold text-forest mb-3", isRTL && "text-start font-arabic")}>
                  {t.sulfur.content.industrialOutput}
                </h3>
                <p className={clsx("text-forest/70 font-normal text-sm md:text-base leading-relaxed", isRTL && "text-start")}>
                  {t.sulfur.content.industrialOutputDesc}
                </p>
              </StaggerItem>

              <StaggerItem className={clsx("border-forest/10 hover:border-gold transition-colors pt-2 pb-2", isRTL ? "border-r-2 pr-6" : "border-l-2 pl-6")}>
                <h3 className={clsx("text-xl font-serif font-bold text-forest mb-3", isRTL && "text-start font-arabic")}>
                  {t.sulfur.content.purityProcessing}
                </h3>
                <p className={clsx("text-forest/70 font-normal text-sm md:text-base leading-relaxed", isRTL && "text-start")}>
                  {t.sulfur.content.purityProcessingDesc}
                </p>
              </StaggerItem>

              <StaggerItem className={clsx("border-forest/10 hover:border-gold transition-colors pt-2 pb-2", isRTL ? "border-r-2 pr-6" : "border-l-2 pl-6")}>
                <h3 className={clsx("text-xl font-serif font-bold text-forest mb-3", isRTL && "text-start font-arabic")}>
                  {t.common.globalLogistics}
                </h3>
                <p className={clsx("text-forest/70 font-normal text-sm md:text-base leading-relaxed", isRTL && "text-start")}>
                  {t.sulfur.content.supplyChainDesc}
                </p>
              </StaggerItem>
            </StaggerContainer>
          </div>
        </div>
      </section>
    </div>
  );
}
