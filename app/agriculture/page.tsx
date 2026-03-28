"use client";

import Image from "next/image";
import Link from "next/link";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Wheat, Droplets, Ship } from "lucide-react";
import { useLanguage } from "@/components/LanguageContext";
import { translations } from "@/lib/translations";
import clsx from "clsx";

export default function AgriculturePage() {
  const { lang, isRTL } = useLanguage();
  const t = translations[lang];

  const lifecycleSteps = [
    {
      num: "01",
      title: t.home.agri.grainExports.title,
      desc: t.home.agri.grainExports.desc,
      icon: Wheat,
    },
    {
      num: "02",
      title: lang === 'ar' ? "اختبارات الجودة" : "Surveyor Testing",
      desc: t.home.agri.surveyorTesting.desc,
      icon: Droplets,
    },
    {
      num: "03",
      title: t.home.agri.logistics.title,
      desc: t.home.agri.logistics.desc,
      icon: Ship,
    },
  ];

  return (
    <div className="bg-offwhite flex flex-col min-h-screen">
      {/* 1. HERO SECTION */}
      <section className="relative w-full h-[70vh] min-h-[500px] flex items-center overflow-hidden bg-forest">
        <div className="absolute inset-0 z-0">
          <Image
            src="/images/wheat_brays_hero.png"
            alt="Medium-Hard Wheat Field"
            fill
            priority
            className="object-cover object-center opacity-40 hover:opacity-60 transition-opacity duration-1000 saturate-150"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6 flex items-center gap-3">
              <Wheat className="w-6 h-6 text-gold" />
              <span className="text-gold font-serif italic tracking-wide">
                {t.agriculture.hero.titleGold}
              </span>
            </StaggerItem>
            <StaggerItem direction="up" className="mb-6">
              <h1 className={clsx("text-5xl md:text-7xl lg:text-8xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.85]", isRTL && "font-arabic")}>
                {lang === 'ar' ? <>الزراعة <br /> العالمية</> : <>Global <br /> Agriculture</>}
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className="text-offwhite/80 text-base md:text-lg font-normal leading-relaxed max-w-xl text-balance">
                {t.agriculture.hero.desc}
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

      {/* 2. SUPPLY CHAIN TIMELINE */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite">
        <div className="container mx-auto px-4 md:px-8">
          <AnimatedSection direction="up" className="mb-16 md:mb-24 text-center">
            <h2 className={clsx("text-4xl md:text-6xl font-serif font-bold text-forest uppercase tracking-tighter", isRTL && "font-arabic")}>
              {lang === 'ar' ? <>سلسلة <span className="text-gold italic font-normal font-sans">التوريد.</span></> : <>Supply <span className="text-gold italic font-normal">Chain.</span></>}
            </h2>
            <div className="w-24 h-px bg-gold mx-auto mt-8" />
          </AnimatedSection>

          <div className="relative max-w-5xl mx-auto">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-12 left-0 right-0 h-px bg-forest/20 z-0" />

            <StaggerContainer className="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-8 relative z-10">
              {lifecycleSteps.map((step, idx) => {
                const Icon = step.icon;
                return (
                  <StaggerItem
                    key={step.num}
                    direction="up"
                    className="relative group bg-white p-8 border border-forest/10 rounded-sm shadow-sm hover:shadow-xl transition-shadow duration-500"
                  >
                    <div className="w-16 h-16 bg-forest text-gold rounded-full flex items-center justify-center mb-8 md:-translate-y-16 mx-auto md:mx-0 group-hover:scale-110 transition-transform duration-500 shadow-lg border-4 border-offwhite">
                      <Icon className="w-8 h-8" />
                    </div>
                    <div className="text-gold font-mono text-sm tracking-widest font-bold mb-2 text-center md:text-left dir-ltr" style={{ direction: 'ltr' }}>
                      {step.num}
                    </div>
                    <h3 className={clsx("text-2xl font-serif font-bold text-forest mb-4 text-center md:text-left", isRTL && "text-start font-arabic")}>
                      {step.title}
                    </h3>
                    <p className={clsx("text-forest/70 font-normal leading-relaxed text-sm text-center md:text-left text-balance", isRTL && "text-start")}>
                      {step.desc}
                    </p>
                  </StaggerItem>
                );
              })}
            </StaggerContainer>
          </div>
        </div>
      </section>

      {/* 3. OPERATIONS GALLERY */}
      <section className="py-24 bg-forest relative overflow-hidden">
        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <AnimatedSection direction="up" className="mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
            <h2 className={clsx("text-3xl md:text-5xl font-serif font-bold text-offwhite uppercase tracking-tighter", isRTL && "font-arabic")}>
              {lang === 'ar' ? <>العمليات <span className="text-gold italic font-normal font-sans">العالمية.</span></> : <>Global <span className="text-gold italic font-normal">Operations.</span></>}
            </h2>
            <p className={clsx("text-offwhite/50 font-normal max-w-md text-balance text-sm md:text-base", isRTL && "text-start")}>
              {lang === 'ar' ? "نعمل بحجم غير مسبوق لإدارة صادرات الحبوب والخدمات اللوجستية المعتمدة من الفاحصين في جميع أنحاء العالم." : "Operating at unprecedented scale to manage grain exports and surveyor-certified logistics worldwide."}
            </p>
          </AnimatedSection>

          {/* CSS Grid with Masonry effect fallback */}
          <StaggerContainer className="grid grid-cols-1 md:grid-cols-12 gap-4 md:grid-rows-[300px_300px]">
             {/* Large Image */}
             <StaggerItem className="md:col-span-8 md:row-span-2 relative group overflow-hidden rounded-sm min-h-[400px] md:min-h-0">
              <Image
                src="/images/wheat_loading.png"
                alt="Wheat Logistics"
                fill
                className="object-cover object-center opacity-90 group-hover:opacity-100 transition-all duration-1000 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/90 via-transparent to-transparent" />
              <div className="absolute bottom-0 left-0 p-8 w-full transition-all duration-500">
                <span className="text-gold text-xs tracking-widest uppercase font-bold mb-2 block">
                  {lang === 'ar' ? "تكامل الخدمات اللوجستية" : "Logistics Integration"}
                </span>
                <h3 className="text-xl md:text-2xl font-serif font-bold text-offwhite">
                  {lang === 'ar' ? "توزيع سفن الصب" : "Bulk Carrier Distribution"}
                </h3>
              </div>
            </StaggerItem>

            {/* Small Top Image */}
            <StaggerItem className="md:col-span-4 md:row-span-1 relative group overflow-hidden rounded-sm min-h-[300px] md:min-h-0">
              <Image
                src="/images/harvesting_brays_hero_product.png"
                alt="Grain Harvesting"
                fill
                className="object-cover object-center opacity-90 group-hover:opacity-100 transition-all duration-1000 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/90 via-transparent to-transparent" />
              <div className="absolute bottom-0 left-0 p-6 w-full">
                <h3 className="text-lg font-serif font-bold text-offwhite">
                  {lang === 'ar' ? "حصاد واسع النطاق" : "Mass Scale Harvesting"}
                </h3>
              </div>
            </StaggerItem>

            {/* Solid Color / Text Block */}
            <StaggerItem className="md:col-span-4 md:row-span-1 bg-gold text-forest p-8 rounded-sm flex flex-col justify-center group relative overflow-hidden min-h-[300px] md:min-h-0">
              <div className="absolute inset-0 m-auto flex items-center justify-center opacity-15 pointer-events-none">
                <Wheat className="w-48 h-48 -translate-y-4" />
              </div>
              <h3 className="text-2xl font-serif font-bold mb-4 z-10 relative">
                {lang === 'ar' ? "معتمد من الفاحصين" : "Surveyor Certified"}
              </h3>
              <p className={clsx("font-medium text-sm text-forest/80 z-10 relative max-w-[200px]", isRTL && "text-start")}>
                {lang === 'ar' ? "عتبات نقاء رائدة في الصناعة للتجارة الدولية." : "Industry-leading purity thresholds for international trade."}
              </p>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>
    </div>
  );
}
