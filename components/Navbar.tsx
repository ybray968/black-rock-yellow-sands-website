"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { COMPANY } from "@/lib/siteData";
import { Menu, X, ArrowRight, Languages } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import clsx from "clsx";
import { useLanguage } from "./LanguageContext";
import { translations } from "@/lib/translations";

import Image from "next/image";

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const pathname = usePathname();
  const { lang, setLang, isRTL } = useLanguage();
  const t = translations[lang];

  const DIVISIONS = [
    { name: t.nav.agriculture, href: "/agriculture", key: "Agriculture" },
    { name: t.nav.construction, href: "/construction", key: "Construction" },
    { name: t.nav.sulfur, href: "/sulfur", key: "Sulfur" },
    { name: t.nav.about, href: "/about", key: "About" },
    { name: t.nav.careers, href: "/careers", key: "Careers" },
    { name: t.common.contact, href: "/contact", key: "Contact" },
  ];

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const getActiveKey = () => {
    if (pathname === "/about") return "About";
    if (pathname === "/contact") return "Contact";
    if (pathname === "/careers") return "Careers";
    if (pathname === "/construction") return "Construction";
    if (pathname === "/sulfur") return "Sulfur";
    if (pathname === "/agriculture") return "Agriculture";
    return "";
  };

  const [hoveredKey, setHoveredKey] = useState<string | null>(null);
  const activeKey = getActiveKey();

  return (
    <>
      <header
        className={clsx(
          "z-50 transition-all duration-500",
          "md:fixed md:top-0 md:left-0 md:right-0",
          "sticky top-0",
          isScrolled
            ? "bg-forest/80 backdrop-blur-xl shadow-premium py-2 text-offwhite border-b border-white/5"
            : "bg-forest/60 backdrop-blur-lg py-4 text-offwhite md:bg-forest/30 md:backdrop-blur-sm shadow-sm"
        )}
      >
        <div className="container mx-auto px-6 md:px-12 flex justify-between md:flex-row items-center">
          {/* Logo */}
          <Link href="/" className="flex items-center group gap-3 justify-self-start -ml-2">
            <div className="relative h-12 w-12 filter drop-shadow-md">
              <Image
                src="/images/braysint-logo-large.png"
                alt="BRAY International Logo"
                fill
                className="object-contain object-left transition-transform duration-500 group-hover:scale-105"
                priority
              />
            </div>
            <div className={clsx("flex flex-col", isRTL ? "pr-0" : "pl-0")}>
              <span className="font-serif font-bold text-xs sm:text-sm tracking-[0.1em] leading-tight text-white/95 whitespace-nowrap uppercase">
                {lang === 'ar' ? "بلاك روك آند يلو ساندز" : "Black Rock And Yellow Sands"}
              </span>
              <span className="text-[10px] premium-tracking text-gold uppercase mt-1">
                {lang === 'ar' ? "إنترناشيونال" : "International"}
              </span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav 
            className="hidden md:flex items-center gap-1 bg-white/5 backdrop-blur-md p-1.5 rounded-full border border-white/10 mx-auto shadow-inner"
            onMouseLeave={() => setHoveredKey(null)}
          >
            {DIVISIONS.map((div) => {
              const isActive = activeKey === div.key;
              const isHovered = hoveredKey === div.key;
              
              return (
                <Link
                  key={div.key}
                  href={div.href}
                  onMouseEnter={() => setHoveredKey(div.key)}
                  className={clsx(
                    "relative px-6 py-2 rounded-full text-xs font-semibold premium-tracking transition-all duration-300 uppercase",
                    isActive ? "text-forest" : "text-offwhite/80 hover:text-offwhite"
                  )}
                >
                  {(isActive || isHovered) && (
                    <motion.div
                      layoutId="nav-pill"
                      className={clsx(
                        "absolute inset-0 rounded-full -z-10 shadow-lg",
                        isActive ? "bg-gold" : "bg-white/10"
                      )}
                      transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                    />
                  )}
                  {div.name}
                </Link>
              );
            })}
            
            <Link
              href="/contact"
              onMouseEnter={() => setHoveredKey("Contact")}
              className={clsx(
                "relative px-6 py-2 rounded-full text-xs font-semibold premium-tracking transition-all duration-300 ml-1 uppercase",
                activeKey === "Contact" ? "text-forest" : "text-gold hover:text-gold"
              )}
            >
              {(activeKey === "Contact" || hoveredKey === "Contact") && (
                <motion.div
                  layoutId="nav-pill"
                  className={clsx(
                    "absolute inset-0 rounded-full -z-10 shadow-lg",
                    activeKey === "Contact" ? "bg-gold" : "bg-white/10"
                  )}
                  transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                />
              )}
              {t.common.contact}
            </Link>
          </nav>

          <div className="flex items-center gap-4">
            {/* Desktop Language Toggle */}
            <div className="hidden md:block">
              <button
                onClick={() => setLang(lang === "en" ? "ar" : "en")}
                className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-[10px] font-bold uppercase premium-tracking hover:bg-gold hover:text-forest transition-all"
              >
                <Languages className="w-3.5 h-3.5" />
                <span>{lang === "en" ? "عربي" : "EN"}</span>
              </button>
            </div>

            {/* Mobile menu button */}
            <button
              className="md:hidden flex items-center justify-center p-2.5 bg-white/10 text-white rounded-full transition-all hover:bg-gold hover:text-forest relative z-[60] border border-white/10"
              onClick={() => setMobileMenuOpen(true)}
              aria-label="Open menu"
            >
              <Menu className="w-6 h-6" />
            </button>
          </div>
        </div>
      </header>

      {/* Mobile Menu Overlay */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 1.02 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 1.02 }}
            transition={{ duration: 0.2 }}
            className="fixed inset-0 bg-forest/98 backdrop-blur-3xl text-offwhite z-[9999] p-6 flex flex-col"
          >
            <div className="flex justify-between items-center mb-6 pb-4 border-b border-white/10">
              <div className="flex items-center gap-4">
                <div className="relative h-10 w-10">
                  <Image
                    src="/images/braysint-logo-large.png"
                    alt="BRAY International Logo"
                    fill
                    className="object-contain"
                  />
                </div>
                {/* Mobile Language Toggle */}
                <button
                  onClick={() => setLang(lang === "en" ? "ar" : "en")}
                  className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/10 border border-white/20 text-[10px] font-bold uppercase premium-tracking hover:bg-gold hover:text-forest transition-all"
                >
                  <Languages className="w-3.5 h-3.5" />
                  <span>{lang === "en" ? "عربي" : "EN"}</span>
                </button>
              </div>
              <button
                onClick={() => setMobileMenuOpen(false)}
                className="p-3 hover:bg-white/10 rounded-full transition-colors border border-white/20"
                aria-label="Close menu"
              >
                <X className="w-6 h-6" />
              </button>
            </div>
            
            <div className="flex flex-col flex-1">
              <div className="mb-8">
                <Link
                  href="/contact"
                  onClick={() => setMobileMenuOpen(false)}
                  className="w-full py-4 bg-gold text-forest font-black tracking-[0.2em] text-[10px] rounded-sm hover:bg-offwhite transition-all uppercase flex items-center justify-center gap-2 shadow-2xl"
                >
                  <span>{t.common.requestAQuote}</span>
                  <ArrowRight className={clsx("w-3 h-3", isRTL && "rotate-180")} />
                </Link>
              </div>

              <div className="flex flex-col gap-1 text-start">
                <h4 className="text-[10px] uppercase tracking-[0.3em] text-gold/60 font-bold mb-4 font-serif italic">
                  {t.common.navigation}
                </h4>
                {DIVISIONS.map((div) => (
                  <Link
                    key={div.key}
                    href={div.href}
                    onClick={() => setMobileMenuOpen(false)}
                    className="py-3.5 flex justify-between items-center group border-b border-white/5 last:border-0"
                  >
                    <span className={clsx(
                      "text-lg font-serif transition-colors", 
                      activeKey === div.key ? "text-gold" : "text-white group-hover:text-gold"
                    )}>
                      {div.name}
                    </span>
                    <ArrowRight className={clsx(
                      "w-4 h-4 transition-all text-gold",
                      isRTL && "rotate-180",
                      activeKey === div.key ? "opacity-100 translate-x-0" : "opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0"
                    )} />
                  </Link>
                ))}
              </div>

              <div className="mt-auto pt-8 text-[10px] uppercase tracking-[0.3em] text-white/30 font-medium">
                <p>{t.common.copyright}</p>
                <p className="mt-1 text-gold/40">{t.footer.tagline.slice(1, 40)}...</p>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
