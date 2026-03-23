"use client";

import Image from "next/image";
import Link from "next/link";
import { motion, useScroll, useTransform } from "framer-motion";
import { useRef, useEffect, useState } from "react";
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

  const videoRef = useRef<HTMLVideoElement>(null);

  const steelY = useTransform(scrollYProgress, [0, 1], ["-15%", "15%"]);
  const plywoodY = useTransform(scrollYProgress, [0, 1], ["5%", "-5%"]);

  return (
    <>
      {/* 1. HERO SECTION: The Bridge */}
      <section className="relative w-full h-screen min-h-[700px] flex overflow-hidden bg-forest">
        {/* Main Background - Bulker Ship */}
        <div className="absolute inset-0 z-0 hidden md:block">
          <video
            ref={videoRef}
            src="/images/hero_water.mp4"
            autoPlay
            loop
            muted
            playsInline
            className="absolute inset-0 w-full h-full object-cover object-center opacity-80"
          />
          <div className="absolute inset-0 bg-forest/40 md:bg-forest/50 mix-blend-multiply" />
          <div className="absolute inset-0 bg-gradient-to-t from-forest via-transparent to-forest/30" />
          {/* Subtle radial glow */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(15,26,18,0.4)_100%)]" />
        </div>

        {/* Content Layers */}
        <div className="relative z-10 w-full flex flex-col md:flex-row">
          {/* Agri Left */}
          <div className="flex-1 flex flex-col justify-end p-10 md:p-20 border-b md:border-b-0 md:border-r border-white/5 group relative overflow-hidden">
            {/* Hover Background Reveal */}
            <div className="absolute inset-0 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity duration-1000 z-0">
              <Image
                src="/images/wheat_brays_hero.png"
                alt="Medium-Hard Wheat Field"
                fill
                className="object-cover object-center scale-105 group-hover:scale-100 transition-transform duration-[2000ms]"
              />
              <div className="absolute inset-0 bg-forest/80" />
            </div>

            <AnimatedSection direction="up" delay={0.2} className="relative z-10 w-full max-w-lg">
              <span className="text-gold font-serif italic mb-6 block flex items-center gap-3 premium-tracking text-xs uppercase">
                <Wheat className="w-5 h-5" /> Division I
              </span>
              <h2 className="text-4xl md:text-5xl lg:text-7xl font-serif font-bold text-offwhite uppercase tracking-tight leading-[0.85] mb-8 text-shadow-premium">
                Agricultural <br /> <span className="text-gold/90">Wholesale</span>
              </h2>
              <p className="text-offwhite/70 font-normal text-base md:text-lg leading-relaxed mb-10 max-w-sm text-balance">
                Sourcing, surveying, and exporting the finest medium-hard wheat and
                agricultural commodities globally.
              </p>
              <Link
                href="/agriculture"
                className="inline-flex items-center space-x-3 text-offwhite hover:text-gold transition-all font-semibold text-xs tracking-[0.2em] uppercase group/link py-2 border-b border-white/10 hover:border-gold"
              >
                <span>Explore Agriculture</span>
                <ArrowRight className="w-4 h-4 transform group-hover/link:translate-x-2 transition-transform" />
              </Link>
            </AnimatedSection>
          </div>

          {/* Construction Right */}
          <div className="flex-1 flex flex-col justify-end p-10 md:p-20 group relative overflow-hidden border-t md:border-t-0 border-white/5">
            <div className="absolute inset-0 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity duration-1000 z-0">
              <Image
                src="/images/steel_brays_hero_product.png"
                alt="Structural Steel"
                fill
                className="object-cover object-center scale-105 group-hover:scale-100 transition-transform duration-[2000ms]"
              />
              <div className="absolute inset-0 bg-slate/90" />
            </div>

            <AnimatedSection direction="up" delay={0.4} className="relative z-10 w-full max-w-lg">
              <span className="text-slate-300 font-serif italic mb-6 block flex items-center gap-3 premium-tracking text-xs uppercase">
                <HardHat className="w-5 h-5" /> Division II
              </span>
              <h2 className="text-4xl md:text-5xl lg:text-7xl font-serif font-bold text-offwhite uppercase tracking-tight leading-[0.85] mb-8 text-shadow-premium">
                Industrial <br /> <span className="text-slate-400">Construction</span>
              </h2>
              <p className="text-offwhite/70 font-normal text-base md:text-lg leading-relaxed mb-10 max-w-sm text-balance">
                Providing elite construction materials from high-strength steel to industrial plywood, with clients' needs in mind.
              </p>
              <Link
                href="/construction"
                className="inline-flex items-center space-x-3 text-offwhite hover:text-gold transition-all font-semibold text-xs tracking-[0.2em] uppercase group/link py-2 border-b border-white/10 hover:border-gold"
              >
                <span>Explore Construction</span>
                <ArrowRight className="w-4 h-4 transform group-hover/link:translate-x-2 transition-transform" />
              </Link>
            </AnimatedSection>
          </div>
        </div>
      </section>

      {/* 2. AGRI-WHOLESALE SECTION */}
      <section id="agri" className="py-32 md:py-48 bg-offwhite relative z-10 overflow-hidden">
        <div className="container mx-auto px-6 md:px-12">
          <AnimatedSection direction="up" className="mb-20 md:mb-32">
            <h2 className="text-5xl md:text-8xl font-serif font-bold text-forest uppercase tracking-tighter leading-none">
              Global <span className="text-gold italic font-normal">Agriculture.</span>
            </h2>
            <p className="text-forest/60 max-w-2xl mt-8 text-xl font-normal leading-relaxed text-balance border-l border-gold pl-8">
              We manage the entire lifecycle from field to surveyor testing to logistics,
              ensuring absolute quality in agricultural wholesale.
            </p>
          </AnimatedSection>

          {/* Bento Grid */}
          <StaggerContainer className="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8 auto-rows-[400px] md:auto-rows-[500px]">
            {/* Grain Exports */}
            <StaggerItem className="relative col-span-1 md:col-span-2 rounded-sm overflow-hidden group shadow-premium">
              <Image
                src="/images/harvesting_brays_hero_product.png"
                alt="Grain Harvesting"
                fill
                className="object-cover object-center transition-transform duration-[2000ms] group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/95 via-forest/20 to-transparent" />
              <div className="absolute bottom-0 left-0 p-12 w-full">
                <div className="glass-morphism inline-flex p-3 rounded-full mb-6">
                  <Wheat className="text-gold w-6 h-6" />
                </div>
                <h3 className="text-3xl md:text-4xl font-serif font-bold text-offwhite mb-4">
                  Grain Exports
                </h3>
                <p className="text-offwhite/70 font-normal text-base max-w-md leading-relaxed">
                  Mass scale harvesting and preparation of high-yield crops for international distribution.
                </p>
              </div>
            </StaggerItem>

            {/* Quality Testing (Text/Image Card) */}
            <StaggerItem className="relative bg-forest text-offwhite rounded-sm overflow-hidden group shadow-premium">
              <Image
                src="/images/grain_surveyor_quality.png"
                alt="Grain Quality Testing"
                fill
                className="object-cover object-center transition-all duration-[2000ms] group-hover:scale-105 opacity-80 group-hover:opacity-100"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-forest/95 via-forest/40 to-transparent" />
              <div className="absolute inset-0 p-10 flex flex-col justify-end">
                <div className="glass-morphism inline-flex p-3 rounded-full mb-auto self-start">
                  <Droplets className="text-gold w-6 h-6" />
                </div>
                <h3 className="text-2xl md:text-3xl font-serif font-bold mb-4 z-10 text-offwhite tracking-tight">
                  Surveyor <br /> Testing
                </h3>
                <p className="text-offwhite/70 font-normal text-sm z-10 leading-relaxed">
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
        className="py-32 md:py-48 bg-forest text-offwhite relative overflow-hidden"
      >
        {/* Decorative background element */}
        <div className="absolute top-0 right-0 w-1/2 h-full bg-slate/10 -skew-x-12 translate-x-1/4 z-0" />

        <div className="container mx-auto px-6 md:px-12 relative z-10">
          <AnimatedSection direction="up" className="mb-20 md:mb-32 flex flex-col md:flex-row md:items-end justify-between gap-12">
            <div className="max-w-3xl">
              <h2 className="text-5xl md:text-8xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-none">
                Industrial <br /> <span className="text-slate-400 italic font-normal">Materials.</span>
              </h2>
              <p className="text-offwhite/60 mt-8 text-xl font-normal leading-relaxed text-balance border-l border-slate-500 pl-8">
                High-contrast execution. We supply the skeletal strength and
                formwork materials for your demanding projects, exactly when you need them.
              </p>
            </div>
            <Link
              href="/construction"
              className="inline-flex items-center space-x-4 text-gold hover:text-offwhite transition-all font-bold tracking-[0.2em] uppercase border-2 border-gold/30 hover:border-offwhite px-10 py-5 rounded-full backdrop-blur-sm hover:bg-gold hover:text-forest shadow-premium group"
            >
              <span>View Division</span>
              <ArrowRight className="w-5 h-5 group-hover:translate-x-2 transition-transform" />
            </Link>
          </AnimatedSection>

          {/* Construction Grid with Parallax */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20 items-center">
            {/* Left side text items */}
            <StaggerContainer className="flex flex-col gap-24">
              <Link href="/sulfur" className="flex flex-col gap-10 group/card">
                <StaggerItem className="border-l-2 border-gold pl-8">
                  <span className="text-gold font-mono text-xs tracking-[0.3em] uppercase mb-4 block opacity-60">
                    01
                  </span>
                  <h3 className="text-3xl md:text-4xl font-serif font-bold mb-4 tracking-tight group-hover/card:text-gold transition-colors">
                    Granular Sulfur
                  </h3>
                  <p className="text-offwhite/50 font-normal text-lg leading-relaxed max-w-md">
                    High-purity industrial grade sulfur optimized for chemical and fertilizer synthesis.
                  </p>
                </StaggerItem>
                <StaggerItem className="relative h-64 md:h-80 overflow-hidden rounded-sm group shadow-premium">
                  <Image
                    src="/images/granular_sulfur.jpg"
                    alt="Granular Sulfur"
                    fill
                    className="object-cover object-center opacity-80 group-hover:opacity-100 transition-all duration-1000 group-hover:scale-110"
                  />
                  <div className="absolute inset-0 bg-forest/40 group-hover:bg-transparent transition-colors duration-1000" />
                  <div className="absolute inset-0 border border-white/5 pointer-events-none" />
                </StaggerItem>
              </Link>

              <Link href="/construction" className="flex flex-col gap-10 group/card">
                <StaggerItem className="border-l-2 border-white/10 pl-8 group-hover/card:border-white/30 transition-colors">
                  <span className="text-white/30 font-mono text-xs tracking-[0.3em] uppercase mb-4 block">
                    02
                  </span>
                  <h3 className="text-3xl md:text-4xl font-serif font-bold mb-4 tracking-tight text-white/90 group-hover/card:text-white transition-colors">
                    Industrial Plywood
                  </h3>
                  <p className="text-offwhite/40 font-normal text-lg leading-relaxed max-w-md">
                    Elite grade engineered plywood sourced for reliable, large-scale structural formwork.
                  </p>
                </StaggerItem>
                <StaggerItem className="relative h-64 md:h-80 overflow-hidden rounded-sm group shadow-premium">
                  <motion.div
                    style={{ y: plywoodY }}
                    className="absolute inset-0 -top-[15%] -bottom-[15%]"
                  >
                    <Image
                      src="/images/plywood_deck_construction_use.png"
                      alt="Plywood Formwork"
                      fill
                      className="object-cover object-center opacity-80 group-hover:opacity-100 transition-all duration-1000 group-hover:scale-110"
                    />
                    <div className="absolute inset-0 bg-forest/40 group-hover:bg-transparent transition-colors duration-1000" />
                  </motion.div>
                </StaggerItem>
              </Link>
            </StaggerContainer>

            {/* Right side steel parallax */}
            <Link href="/construction" className="relative h-[700px] md:h-[900px] overflow-hidden ml-auto w-full md:w-11/12 rounded-sm block group/card shadow-premium border border-white/5">
              <motion.div
                style={{ y: steelY }}
                className="absolute inset-0 -top-[20%] -bottom-[20%]"
              >
                <Image
                  src="/images/steel_brays_hero_product.png"
                  alt="Rising Structural Steel"
                  fill
                  className="object-cover object-center opacity-80 group-hover:opacity-100 transition-all duration-[2000ms] group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-forest via-transparent to-forest/30" />
              </motion.div>

              <div className="absolute bottom-16 left-0 right-0 px-12">
                <span className="text-slate-400 font-mono text-xs tracking-[0.3em] uppercase mb-4 block">
                  03
                </span>
                <h3 className="text-4xl md:text-5xl font-serif font-bold text-offwhite mb-6 leading-tight tracking-tighter">
                  Structural Steel
                </h3>
                <p className="text-offwhite/60 font-normal text-lg max-w-sm leading-relaxed">
                  Heavy-duty steel frameworks supplied for monumental infrastructure and maximum load capacities.
                </p>
                <div className="mt-10 h-1 w-20 bg-gold/50 group-hover/card:w-40 transition-all duration-700" />
              </div>
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
