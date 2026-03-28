"use client";

import Link from "next/link";
import Image from "next/image";
import { COMPANY } from "@/lib/siteData";
import { useLanguage } from "./LanguageContext";
import { translations } from "@/lib/translations";
import clsx from "clsx";

export default function Footer() {
  const { lang, isRTL } = useLanguage();
  const t = translations[lang];

  return (
    <footer id="contact" className={clsx("bg-forest text-offwhite border-t border-white/5 mt-auto py-16 relative overflow-hidden", isRTL && "font-arabic")}>
      {/* Decorative Top Border Gradient */}
      <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-gold/50 to-transparent" />
      
      <div className="container mx-auto px-6 md:px-12 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 lg:gap-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <Link href="/" className="flex items-center group gap-4 mb-8 -ml-2">
              <div className="relative h-12 w-12 transition-all duration-500">
                <Image
                  src="/images/braysint-logo-large.png"
                  alt="BRAY International Logo"
                  fill
                  className="object-contain object-left"
                />
              </div>
              <div className="flex flex-col">
                <span className="font-serif font-bold text-lg tracking-tight leading-none text-white/95 uppercase">
                  {lang === 'ar' ? "بلاك روك آند يلو ساندز" : "Black Rock And Yellow Sands"}
                </span>
                <span className="text-[10px] md:text-xs premium-tracking text-gold uppercase mt-1">
                  {lang === 'ar' ? "إنترناشيونال" : "International"}
                </span>
              </div>
            </Link>
            <p className="text-white/40 max-w-md font-normal text-sm md:text-base leading-relaxed text-balance italic">
              {t.footer.tagline}
            </p>
          </div>

          {/* Contact Information */}
          <div className="space-y-8">
            <h3 className="font-serif font-bold text-[10px] premium-tracking uppercase text-gold border-b border-gold/20 pb-4 inline-block">
              {t.footer.communication}
            </h3>
            <ul className="space-y-4 text-sm font-normal">
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/40 font-serif italic mb-1">
                  {t.footer.primaryEmail}
                </span>
                <a
                  href={`mailto:${COMPANY.email}`}
                  className={clsx("hover:text-gold transition-colors block text-white font-semibold text-xs lowercase dir-ltr", isRTL ? "text-right" : "text-left")}
                  style={{ direction: 'ltr' }}
                >
                  {COMPANY.email}
                </a>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/40 font-serif italic mb-1">
                  {t.footer.directLine}
                </span>
                <a
                  href={`tel:${COMPANY.phone}`}
                  className={clsx("hover:text-gold transition-colors block text-white font-semibold text-xs tracking-wide dir-ltr", isRTL ? "text-right" : "text-left")}
                  style={{ direction: 'ltr' }}
                >
                  {COMPANY.phone}
                </a>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/40 font-serif italic mb-1">
                  {t.footer.globalHq}
                </span>
                <address className={clsx("not-italic text-white font-semibold text-xs leading-relaxed max-w-[240px]", isRTL ? "text-right" : "text-left")}>
                  {COMPANY.address}
                </address>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/40 font-serif italic mb-3">
                  {t.footer.credentials}
                </span>
                <div className={clsx("flex flex-col gap-1 text-white font-semibold text-xs uppercase w-full", isRTL ? "items-start text-right" : "items-start text-left")}>
                  <span className={clsx("dir-ltr block w-full", isRTL ? "text-right" : "text-left")} style={{ direction: 'ltr' }}>CR: {COMPANY.cr}</span>
                  <span className={clsx("dir-ltr block w-full", isRTL ? "text-right" : "text-left")} style={{ direction: 'ltr' }}>VATIN: {COMPANY.vat}</span>
                </div>
              </li>
            </ul>
          </div>

          {/* Sectors */}
          <div className="space-y-8">
            <h3 className="font-serif font-bold text-[10px] premium-tracking uppercase text-gold border-b border-gold/20 pb-4 inline-block">
              {t.footer.sectors}
            </h3>
            <ul className="space-y-4 text-sm font-normal">
              {COMPANY.divisions.map((div) => (
                <li key={div.name}>
                  <Link
                    href={div.href}
                    className="text-white/40 hover:text-gold transition-all hover:translate-x-1 inline-block uppercase text-xs font-bold tracking-widest"
                  >
                    {lang === 'ar' 
                      ? (div.name === "Agriculture" ? "الزراعة" : div.name === "Industrial Construction" ? "الإنشاءات الصناعية" : "تجارة الكبريت")
                      : div.name}
                  </Link>
                </li>
              ))}
              <li className="pt-4">
                <Link
                  href="/contact"
                  className="text-gold hover:text-white transition-colors uppercase text-xs font-black tracking-[0.2em] border border-gold/30 px-4 py-2 rounded-sm inline-block"
                >
                  {t.common.requestAQuote}
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-16 pt-10 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8 text-[11px] font-medium premium-tracking text-white/30 uppercase">
          <p>
            {t.common.copyright}
          </p>
          <div className="flex space-x-10">
            <Link href="/privacy" className="hover:text-gold transition-colors">
              {t.common.privacy}
            </Link>
            <Link href="/terms" className="hover:text-gold transition-colors">
              {t.common.terms}
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
