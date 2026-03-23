"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { COMPANY } from "@/lib/siteData";
import { Menu, X, ArrowRight } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import clsx from "clsx";

import Image from "next/image";

const DIVISIONS = [
  { name: "Agriculture", href: "/agriculture" },
  { name: "Construction", href: "/construction" },
  { name: "Sulfur", href: "/sulfur" },
  { name: "About", href: "/about" },
  { name: "Careers", href: "/careers" },
];

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const getActiveDivision = () => {
    if (pathname === "/about") return "About";
    if (pathname === "/contact") return "Contact";
    if (pathname === "/careers") return "Careers";
    if (pathname === "/construction") return "Construction";
    if (pathname === "/sulfur") return "Sulfur";
    if (pathname === "/agriculture") return "Agriculture";
    return ""; // Default for home page
  };

  const [hoveredLink, setHoveredLink] = useState<string | null>(null);
  const activeLink = getActiveDivision();

  return (
    <header
      className={clsx(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-500",
        isScrolled
          ? "bg-forest/80 backdrop-blur-xl shadow-premium py-3 text-offwhite border-b border-white/5"
          : "bg-transparent py-6 text-offwhite"
      )}
    >
      <div className="container mx-auto px-6 md:px-12 flex justify-between md:grid md:grid-cols-3 items-center">
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
          <div className="flex flex-col pl-0">
            <span className="font-serif font-bold text-xs sm:text-sm tracking-[0.1em] leading-tight text-white/95 whitespace-nowrap uppercase">
              Black Rock And Yellow Sands
            </span>
            <span className="text-[10px] premium-tracking text-gold uppercase mt-1">
              International
            </span>
          </div>
        </Link>

        {/* Desktop Navigation - Division Switcher */}
        <nav 
          className="hidden md:flex items-center gap-1 bg-white/5 backdrop-blur-md p-1.5 rounded-full border border-white/10 justify-self-center shadow-inner"
          onMouseLeave={() => setHoveredLink(null)}
        >
          {DIVISIONS.map((div) => {
            const isActive = activeLink === div.name;
            const isHovered = hoveredLink === div.name;
            
            return (
              <Link
                key={div.name}
                href={div.href}
                onMouseEnter={() => setHoveredLink(div.name)}
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
          
          {/* Contact Button inside the menu */}
          <Link
            href="/contact"
            onMouseEnter={() => setHoveredLink("Contact")}
            className={clsx(
              "relative px-6 py-2 rounded-full text-xs font-semibold premium-tracking transition-all duration-300 ml-1 uppercase",
              activeLink === "Contact" ? "text-forest" : "text-gold hover:text-gold"
            )}
          >
            {(activeLink === "Contact" || hoveredLink === "Contact") && (
              <motion.div
                layoutId="nav-pill"
                className={clsx(
                  "absolute inset-0 rounded-full -z-10 shadow-lg",
                  activeLink === "Contact" ? "bg-gold" : "bg-white/10"
                )}
                transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
              />
            )}
            Contact
          </Link>
        </nav>

        {/* Mobile menu button */}
        <button
          className="md:hidden text-inherit p-2 justify-self-end hover:bg-white/5 rounded-full transition-colors"
          onClick={() => setMobileMenuOpen(true)}
          aria-label="Open menu"
        >
          <Menu className="w-6 h-6" />
        </button>
      </div>

      {/* Mobile Menu Overlay */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ type: "spring", damping: 25, stiffness: 200 }}
            className="absolute top-0 left-0 right-0 bg-forest/98 backdrop-blur-2xl text-offwhite shadow-2xl z-50 p-8 flex flex-col min-h-[60vh] border-b border-white/10"
          >
            <div className="flex justify-between items-center mb-12">
              <div className="relative h-10 w-[180px]">
                <Image
                  src="/images/braysint-logo-large.png"
                  alt="BRAY International Logo"
                  fill
                  className="object-contain object-left"
                />
              </div>
              <button
                onClick={() => setMobileMenuOpen(false)}
                className="p-3 hover:bg-white/10 rounded-full transition-colors border border-white/5 shadow-inner"
                aria-label="Close menu"
              >
                <X className="w-6 h-6" />
              </button>
            </div>
            
            <div className="flex flex-col gap-8 text-2xl font-serif">
              {DIVISIONS.map((div) => (
                <Link
                  key={div.name}
                  href={div.href}
                  onClick={() => setMobileMenuOpen(false)}
                  className="border-b border-white/5 pb-6 flex justify-between items-center group"
                >
                  <span className={clsx("transition-all duration-300 premium-tracking group-hover:translate-x-2", activeLink === div.name ? "text-gold" : "text-offwhite/80 group-hover:text-gold")}>
                    {div.name}
                  </span>
                  <ArrowRight className="w-5 h-5 opacity-0 group-hover:opacity-100 -translate-x-4 group-hover:translate-x-0 transition-all text-gold" />
                </Link>
              ))}
              <Link
                href="/contact"
                onClick={() => setMobileMenuOpen(false)}
                className="border-b border-white/5 pb-6 text-gold/80 hover:text-gold transition-colors mt-12 premium-tracking flex justify-between items-center group"
              >
                <span>CONTACT</span>
                <ArrowRight className="w-5 h-5 opacity-0 group-hover:opacity-100 -translate-x-4 group-hover:translate-x-0 transition-all" />
              </Link>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
