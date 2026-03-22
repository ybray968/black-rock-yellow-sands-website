"use client";

import Image from "next/image";
import Link from "next/link";
import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { ArrowRight, Droplets, HardHat, Wheat } from "lucide-react";

export default function Home() {
  const constructionRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: constructionRef,
    offset: ["start end", "end start"],
  });

  const steelY = useTransform(scrollYProgress, [0, 1], ["-15%", "15%"]);
  const plywoodY = useTransform(scrollYProgress, [0, 1], ["5%", "-5%"]);

  return (
    <>
      {/* 1. HERO SECTION: The Bridge */}
      <section className="relative w-full h-screen min-h-[600px] flex overflow-hidden bg-forest">
        {/* Main Background - Bulker Ship */}
        <div className="absolute inset-0 z-0 hidden md:block">
          <Image
            src="/images/home_hero.png"
            alt="Bulker ship representing global reach"
            fill
            priority
            className="object-cover object-[65%_center] md:object-center"
          />
          <div className="absolute inset-0 bg-forest/80 md:bg-forest/70 mix-blend-multiply" />
          <div className="absolute inset-0 bg-gradient-to-t from-forest via-forest/40 to-transparent" />
        </div>

        {/* Content Layers */}
        <div className="relative z-10 w-full flex flex-col md:flex-row">
          {/* Agri Left */}
          <div className="flex-1 flex flex-col justify-end p-8 md:p-16 border-b md:border-b-0 md:border-r border-white/10 group relative overflow-hidden">
            {/* Hover Background Reveal */}
            <div className="absolute inset-0 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity duration-1000 z-0">
              <Image
                src="/images/wheat_brays_hero.png"
                alt="Medium-Hard Wheat Field"
                fill
                className="object-cover object-center"
              />
              <div className="absolute inset-0 bg-forest/80" />
            </div>

            <AnimatedSection direction="up" delay={0.2} className="relative z-10 w-full max-w-lg">
              <span className="text-gold font-serif italic mb-4 block flex items-center gap-2">
                <Wheat className="w-5 h-5" /> Division I
              </span>
              <h2 className="text-4xl md:text-5xl lg:text-6xl font-serif font-bold text-offwhite uppercase tracking-tight leading-[0.9] mb-6">
                Agricultural <br /> Wholesale
              </h2>
              <p className="text-offwhite/80 font-normal text-sm md:text-base leading-relaxed mb-8 max-w-sm">
                Sourcing, surveying, and exporting the finest medium-hard wheat and
                agricultural commodities globally. <br />&nbsp;
              </p>
              <Link
                href="/agriculture"
                className="inline-flex items-center space-x-2 text-offwhite hover:text-gold transition-colors font-medium text-sm tracking-wide uppercase group/link"
              >
                <span>Explore Agriculture</span>
                <ArrowRight className="w-4 h-4 transform group-hover/link:translate-x-1 transition-transform" />
              </Link>
            </AnimatedSection>
          </div>

          {/* Construction Right */}
          <div className="flex-1 flex flex-col justify-end p-8 md:p-16 group relative overflow-hidden border-t md:border-t-0 border-white/10">
            <div className="absolute inset-0 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity duration-1000 z-0">
              <Image
                src="/images/steel_brays_hero_product.png"
                alt="Structural Steel"
                fill
                className="object-cover object-center"
              />
              <div className="absolute inset-0 bg-slate/90" />
            </div>

            <AnimatedSection direction="up" delay={0.4} className="relative z-10 w-full max-w-lg">
              <span className="text-slate-300 font-serif italic mb-4 block flex items-center gap-2">
                <HardHat className="w-5 h-5" /> Division II
              </span>
              <h2 className="text-4xl md:text-5xl lg:text-6xl font-serif font-bold text-offwhite uppercase tracking-tight leading-[0.9] mb-6">
                Industrial <br /> Construction
              </h2>
              <p className="text-offwhite/80 font-normal text-sm md:text-base leading-relaxed mb-8 max-w-sm">
                Providing elite construction materials—from high-strength steel to industrial plywood—with our customers' structural timeline in mind.
              </p>
              <Link
                href="/construction"
                className="inline-flex items-center space-x-2 text-offwhite hover:text-gold transition-colors font-medium text-sm tracking-wide uppercase group/link"
              >
                <span>Explore Construction</span>
                <ArrowRight className="w-4 h-4 transform group-hover/link:translate-x-1 transition-transform" />
              </Link>
            </AnimatedSection>
          </div>
        </div>
      </section>

      {/* 2. AGRI-WHOLESALE SECTION */}
      <section id="agri" className="py-24 md:py-32 bg-offwhite relative z-10">
        <div className="container mx-auto px-4 md:px-8">
          <AnimatedSection direction="up" className="mb-16 md:mb-24">
            <h2 className="text-4xl md:text-6xl font-serif font-bold text-forest uppercase tracking-tighter">
              Global <span className="text-gold italic font-normal">Agriculture.</span>
            </h2>
            <p className="text-forest/70 max-w-2xl mt-6 text-lg font-normal leading-relaxed text-balance">
              We manage the entire lifecycle from field to surveyor testing to logistics,
              ensuring absolute quality in agricultural wholesale.
            </p>
          </AnimatedSection>

          {/* Bento Grid */}
          <StaggerContainer className="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 auto-rows-[300px] md:auto-rows-[400px]">
            {/* Grain Exports */}
            <StaggerItem className="relative col-span-1 md:col-span-2 rounded-sm overflow-hidden group">
              <Image
                src="/images/harvesting_brays_hero_product.png"
                alt="Grain Harvesting"
                fill
                className="object-cover object-center transition-transform duration-1000 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/90 via-forest/40 to-transparent" />
              <div className="absolute bottom-0 left-0 p-8 w-full">
                <Wheat className="text-gold w-8 h-8 mb-4 opacity-80" />
                <h3 className="text-2xl font-serif font-bold text-offwhite mb-2">
                  Grain Exports
                </h3>
                <p className="text-offwhite/80 font-normal text-sm max-w-md">
                  Mass scale harvesting and preparation of high-yield crops.
                </p>
              </div>
            </StaggerItem>

            {/* Quality Testing (Text/Image Card) */}
            <StaggerItem className="relative bg-forest text-offwhite rounded-sm overflow-hidden group">
              <Image
                src="/images/grain_surveyor_quality.png"
                alt="Grain Quality Testing"
                fill
                className="object-cover object-center transition-all duration-1000 group-hover:scale-105 opacity-90 group-hover:opacity-100"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/90 via-forest/40 to-transparent" />
              <div className="absolute inset-0 p-8 flex flex-col justify-end">
                <Droplets className="text-gold w-8 h-8 mb-auto opacity-80" />
                <h3 className="text-xl md:text-2xl font-serif font-bold mb-3 z-10 text-offwhite">
                  Surveyor <br /> Testing
                </h3>
                <p className="text-offwhite/80 font-normal text-sm z-10">
                  Rigorous international quality control standards applied to every shipment.
                </p>
              </div>
            </StaggerItem>

            {/* Logistics (Image Card) */}
            <StaggerItem className="relative col-span-1 md:col-span-3 rounded-sm overflow-hidden group h-[300px] md:h-auto">
              <Image
                src="/images/wheat_loading.png"
                alt="Wheat Logistics"
                fill
                className="object-cover object-center transition-all duration-1000 group-hover:scale-105 opacity-90 group-hover:opacity-100"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/90 via-forest/30 to-transparent" />
              <div className="absolute bottom-0 left-0 p-8 w-full">
                <h3 className="text-2xl font-serif font-bold text-offwhite mb-2">
                  Global Logistics
                </h3>
                <p className="text-offwhite/80 font-normal text-sm max-w-2xl">
                  Coordinated shipping and distribution using bulk carrier vessels.
                </p>
              </div>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 3. INDUSTRIAL CONSTRUCTION SECTION */}
      <section
        id="construction"
        ref={constructionRef}
        className="py-24 md:py-32 bg-forest text-offwhite relative overflow-hidden"
      >
        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <AnimatedSection direction="up" className="mb-16 md:mb-24 flex flex-col md:flex-row md:items-end justify-between gap-8">
            <div className="max-w-2xl">
              <h2 className="text-4xl md:text-6xl font-serif font-bold text-offwhite uppercase tracking-tighter">
                Industrial <span className="text-slate-400 italic font-normal">Materials.</span>
              </h2>
              <p className="text-offwhite/70 mt-6 text-lg font-normal leading-relaxed text-balance">
                High-contrast execution. We supply the skeletal strength and
                formwork materials for your demanding projects, exactly when you need them.
              </p>
            </div>
            <Link
              href="/construction"
              className="inline-flex items-center space-x-3 text-gold hover:text-offwhite transition-colors font-medium tracking-wide uppercase border border-gold hover:border-offwhite px-6 py-3 rounded-full"
            >
              <span>View Division</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </AnimatedSection>

          {/* Construction Grid with Parallax */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center">
            {/* Left side text items */}
            <StaggerContainer className="flex flex-col gap-16">
              <Link href="/sulfur" className="flex flex-col gap-8 group/card hover:opacity-80 transition-opacity">
                <StaggerItem className="border-l border-gold pl-6">
                  <span className="text-gold font-mono text-xs tracking-widest uppercase mb-2 block">
                    01
                  </span>
                  <h3 className="text-2xl font-serif font-bold mb-3">
                    Granular Sulfur
                  </h3>
                  <p className="text-offwhite/60 font-normal">
                    High-purity industrial grade sulfur optimized for chemical and fertilizer synthesis.
                  </p>
                </StaggerItem>
                <StaggerItem className="relative h-48 md:h-64 overflow-hidden rounded-sm group">
                  <Image
                    src="/images/granular_sulfur.jpg"
                    alt="Granular Sulfur"
                    fill
                    className="object-cover object-center opacity-90 group-hover:opacity-100 transition-all duration-700 group-hover:scale-105"
                  />
                  <div className="absolute inset-0 bg-forest/40 group-hover:bg-transparent transition-colors duration-700" />
                </StaggerItem>
              </Link>

              <Link href="/construction" className="flex flex-col gap-8 group/card hover:opacity-80 transition-opacity">
                <StaggerItem className="border-l border-white/20 pl-6 hover:border-white/50 transition-colors">
                  <span className="text-white/40 font-mono text-xs tracking-widest uppercase mb-2 block">
                    02
                  </span>
                  <h3 className="text-2xl font-serif font-bold mb-3 text-white/80">
                    Industrial Plywood
                  </h3>
                  <p className="text-offwhite/50 font-normal">
                    Elite grade engineered plywood sourced for reliable, large-scale structural formwork.
                  </p>
                </StaggerItem>
                <StaggerItem className="relative h-48 md:h-64 overflow-hidden rounded-sm group">
                  <motion.div
                    style={{ y: plywoodY }}
                    className="absolute inset-0 -top-[10%] -bottom-[10%]"
                  >
                    <Image
                      src="/images/plywood_deck_construction_use.png"
                      alt="Plywood Formwork"
                      fill
                      className="object-cover object-center opacity-90 group-hover:opacity-100 transition-all duration-700 group-hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-forest/40 group-hover:bg-transparent transition-colors duration-700" />
                  </motion.div>
                </StaggerItem>
              </Link>
            </StaggerContainer>

            {/* Right side steel parallax */}
            <Link href="/construction" className="relative h-[600px] md:h-[800px] overflow-hidden ml-auto w-full md:w-5/6 rounded-sm block group/card hover:opacity-90 transition-opacity">
              <motion.div
                style={{ y: steelY }}
                className="absolute inset-0 -top-[15%] -bottom-[15%]"
              >
                <Image
                  src="/images/steel_brays_hero_product.png"
                  alt="Rising Structural Steel"
                  fill
                  className="object-cover object-center opacity-90 hover:opacity-100 transition-all duration-1000"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-forest via-transparent to-forest/30" />
              </motion.div>

              <div className="absolute bottom-12 left-0 right-0 px-8">
                <span className="text-slate-400 font-mono text-xs tracking-widest uppercase mb-2 block">
                  03
                </span>
                <h3 className="text-3xl font-serif font-bold text-offwhite mb-3">
                  Structural Steel
                </h3>
                <p className="text-offwhite/70 font-normal max-w-sm">
                  Heavy-duty steel frameworks supplied for monumental infrastructure and maximum load capacities.
                </p>
              </div>
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
