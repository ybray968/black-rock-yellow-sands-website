"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { COMPANY } from "@/lib/siteData";
import { Menu, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import clsx from "clsx";

import Image from "next/image";

const DIVISIONS = [
  { name: "Agriculture", href: "/agriculture" },
  { name: "Construction", href: "/construction" },
  { name: "Sulfur", href: "/sulfur" },
  { name: "About", href: "/about" },
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
    if (pathname === "/construction") return "Construction";
    if (pathname === "/sulfur") return "Sulfur";
    if (pathname === "/agriculture") return "Agriculture";
    return ""; // Default for home page
  };

  const activeLink = getActiveDivision();

  return (
    <header
      className={clsx(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        isScrolled
          ? "bg-forest/95 backdrop-blur-md shadow-lg py-3 text-offwhite"
          : "bg-transparent py-5 text-offwhite"
      )}
    >
      <div className="container mx-auto px-4 md:px-8 flex justify-between md:grid md:grid-cols-3 items-center">
        {/* Logo */}
        <Link href="/" className="flex items-center group gap-2 justify-self-start -ml-2">
          <div className="relative h-12 w-12">
            <Image
              src="/images/braysint-logo-large.png"
              alt="BRAY International Logo"
              fill
              className="object-contain object-left transition-opacity group-hover:opacity-80"
              priority
            />
          </div>
          <div className="flex flex-col pl-0">
            <span className="font-serif font-bold text-xs sm:text-sm tracking-wide leading-tight text-white/90 whitespace-nowrap">
              BLACK ROCK AND YELLOW SANDS
            </span>
            <span className="text-[10px] tracking-widest text-gold uppercase mt-0.5">
              International
            </span>
          </div>
        </Link>

        {/* Desktop Navigation - Division Switcher */}
        <nav className="hidden md:flex items-center gap-1 bg-white/10 backdrop-blur-sm p-1 rounded-full border border-white/20 justify-self-center">
          {DIVISIONS.map((div) => {
            const isActive = activeLink === div.name;
            return (
              <Link
                key={div.name}
                href={div.href}
                className={clsx(
                  "relative px-5 py-2 rounded-full text-sm font-medium tracking-wide transition-colors",
                  isActive ? "text-forest" : "text-offwhite hover:text-gold"
                )}
              >
                {isActive && (
                  <motion.div
                    layoutId="active-nav-pill"
                    className="absolute inset-0 bg-gold rounded-full -z-10"
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
            className={clsx(
              "px-5 py-2 rounded-full text-sm font-medium tracking-wide transition-colors ml-1",
              activeLink === "Contact"
                ? "bg-white/10 text-gold shadow-sm"
                : "text-gold hover:bg-white/10 hover:text-gold/80"
            )}
          >
            Contact
          </Link>
        </nav>

        {/* Mobile menu button */}
        <button
          className="md:hidden text-inherit p-2 justify-self-end"
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
            className="absolute top-0 left-0 right-0 bg-forest text-offwhite shadow-2xl z-50 p-6 flex flex-col min-h-[50vh]"
          >
            <div className="flex justify-between items-center mb-10">
              <div className="relative h-10 w-[150px]">
                <Image
                  src="/images/braysint-logo-large.png"
                  alt="BRAY International Logo"
                  fill
                  className="object-contain object-left"
                />
              </div>
              <button
                onClick={() => setMobileMenuOpen(false)}
                className="p-2 hover:bg-white/10 rounded-full transition-colors"
                aria-label="Close menu"
              >
                <X className="w-6 h-6" />
              </button>
            </div>
            
            <div className="flex flex-col gap-6 text-xl font-serif">
              {DIVISIONS.map((div) => (
                <Link
                  key={div.name}
                  href={div.href}
                  onClick={() => setMobileMenuOpen(false)}
                  className="border-b border-white/10 pb-4 flex justify-between items-center group"
                >
                  <span className={clsx("transition-colors group-hover:text-gold", activeLink === div.name && "text-gold")}>
                    {div.name}
                  </span>
                </Link>
              ))}
              <Link
                href="/contact"
                onClick={() => setMobileMenuOpen(false)}
                className="border-b border-white/10 pb-4 text-offwhite/70 hover:text-offwhite transition-colors mt-8"
              >
                Contact
              </Link>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
