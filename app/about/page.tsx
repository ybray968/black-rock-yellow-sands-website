"use client";

import Image from "next/image";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Landmark, Compass, Target } from "lucide-react";

export default function AboutPage() {
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
            className="object-cover object-center opacity-40 hover:opacity-60 transition-opacity duration-1000"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6 flex items-center gap-3">
              <Landmark className="w-6 h-6 text-gold" />
              <span className="text-gold font-serif italic tracking-wide">
                Company Profile
              </span>
            </StaggerItem>
            <StaggerItem direction="up" className="mb-6">
              <h1 className="text-5xl md:text-7xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.9]">
                About <br /> Us
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className="text-offwhite/90 text-lg md:text-xl font-normal leading-relaxed max-w-xl text-balance">
                Pioneering quality distribution for global agriculture and
                industrial construction.
              </p>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 2. TEXT CONTENT & CORPORATE STATEMENTS */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite">
        <div className="container mx-auto px-4 md:px-8">

          <div className="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-16 lg:gap-24">

            {/* Left Column: Who We Are */}
            <div className="md:col-span-7 lg:col-span-8">
              <AnimatedSection direction="up" className="mb-12">
                <h2 className="text-4xl md:text-5xl font-serif font-bold text-forest uppercase tracking-tighter mb-8">
                  Who We <span className="text-gold italic font-normal">Are.</span>
                </h2>
                <div className="space-y-6 text-forest/90 font-normal text-lg leading-relaxed text-balance">
                  <p>
                    <strong className="font-bold text-forest">Black Rock And Yellow Sands International</strong> is a
                    premier wholesale supplier operating at the nexus of global trade. We deliver materials of exceptional quality, meeting strict purity thresholds and ISO standards, concerning emissions standards in our products.
                  </p>
                  <p>
                    Our core focus and primary operational division is dedicated to <strong>Agricultural Commodities</strong>, leading with high-quality global wheat distribution. This is followed by our specialized <strong>Granular Sulfur</strong> division powering fertilizer manufacturing, alongside our heavy <strong>Construction Steel</strong> and industrial-grade <strong>Plywood</strong> divisions.
                  </p>
                  <p>
                    As our products fuel critical manufacturing lines and large-scale development projects, where quality is non-negotiable. Every shipment is rigorously analyzed, tested, and certified by internationally recognized surveyors like <strong>SGS, Bureau Veritas, and Intertek</strong>. 
                  </p>
                  <p>
                    We guarantee the integrity of our supply chains from origin to destination. Our commodities and materials are delivered efficiently via a modern vessel fleet, featuring reliable maritime equipment and operated by highly trained, professional staff members.
                  </p>
                </div>
              </AnimatedSection>
            </div>

            {/* Right Column: Vision & Mission */}
            <div className="md:col-span-5 lg:col-span-4 flex flex-col gap-12 border-t md:border-t-0 md:border-l border-forest/10 pt-12 md:pt-0 md:pl-12 lg:pl-16">

              <AnimatedSection direction="left" delay={0.2} className="relative">
                <Compass className="w-8 h-8 text-gold mb-6" />
                <h3 className="text-2xl font-serif font-bold text-forest mb-4">
                  Our Vision
                </h3>
                <p className="text-forest/80 font-normal text-base leading-relaxed text-balance">
                  To be the preferred global wholesale supplier of agricultural
                  commodities, fertilizers, and premium construction materials for
                  manufacturers and developers who demand uncompromising quality and reliable supply chains.
                </p>
              </AnimatedSection>

              <div className="w-12 h-px bg-forest/10" />

              <AnimatedSection direction="left" delay={0.4} className="relative">
                <Target className="w-8 h-8 text-gold mb-6" />
                <h3 className="text-2xl font-serif font-bold text-forest mb-4">
                  Our Mission
                </h3>
                <p className="text-forest/80 font-normal text-base leading-relaxed text-balance">
                  To reliably deliver consistent, high-yield wheat grain, barley,
                  soybean, granular sulfur, structural steel, and construction plywood. 
                  Every shipment undergoes elite international surveyor testing to meet the 
                  highest global standards, powered by sophisticated logistics and competitive wholesale pricing.
                </p>
              </AnimatedSection>

            </div>
          </div>

        </div>
      </section>
    </div>
  );
}
