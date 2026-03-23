import Link from "next/link";
import Image from "next/image";
import { COMPANY } from "@/lib/siteData";

export default function Footer() {
  return (
    <footer id="contact" className="bg-forest text-offwhite border-t border-white/5 mt-auto py-24 relative overflow-hidden">
      {/* Decorative Top Border Gradient */}
      <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-gold/50 to-transparent" />
      
      <div className="container mx-auto px-6 md:px-12 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 lg:gap-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <Link href="/" className="flex items-center group gap-4 mb-10 -ml-2">
              <div className="relative h-14 w-14">
                <Image
                  src="/images/braysint-logo-large.png"
                  alt="BRAY International Logo"
                  fill
                  className="object-contain object-left transition-opacity group-hover:opacity-80"
                />
              </div>
              <div className="flex flex-col pl-0">
                <span className="font-serif font-bold text-base tracking-[0.05em] leading-tight text-white/95 uppercase">
                  Black Rock And Yellow Sands
                </span>
                <span className="text-[11px] premium-tracking text-gold uppercase mt-1.5 opacity-80">
                  International
                </span>
              </div>
            </Link>
            <p className="text-offwhite/50 max-w-md font-normal text-base leading-relaxed text-balance">
              Black Rock And Yellow Sands International LLC. Setting the global standard in high-purity agricultural commodities and structural industrial materials.
            </p>
          </div>

          {/* Contact Information */}
          <div>
            <h3 className="font-serif text-xl font-bold mb-10 text-gold/90 premium-tracking uppercase text-sm">
              Contact
            </h3>
            <ul className="space-y-6 text-base font-normal text-offwhite/60">
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/30 mb-2">
                  Primary Email
                </span>
                <a
                  href={`mailto:${COMPANY.email}`}
                  className="hover:text-gold transition-colors block text-offwhite/80"
                >
                  {COMPANY.email}
                </a>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/30 mb-2">
                  Contact Number
                </span>
                <a
                  href={`tel:${COMPANY.phone}`}
                  className="hover:text-gold transition-colors block text-offwhite/80"
                >
                  {COMPANY.phone}
                </a>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/30 mb-2">
                  Headquarters
                </span>
                <address className="not-italic text-offwhite/80 leading-relaxed uppercase text-xs tracking-wider">
                  {COMPANY.address}
                </address>
              </li>
              <li>
                <span className="block text-[10px] uppercase tracking-[0.2em] text-white/30 mb-4">
                  Credentials
                </span>
                <div className="flex flex-col gap-2 text-offwhite/80">
                  <span className="text-xs uppercase tracking-wider">CR: {COMPANY.cr}</span>
                  <span className="text-xs uppercase tracking-wider">VATIN: {COMPANY.vat}</span>
                </div>
              </li>
            </ul>
          </div>

          {/* Divisions */}
          <div>
            <h3 className="font-serif text-xl font-bold mb-10 text-gold/90 premium-tracking uppercase text-sm">
              Sectors
            </h3>
            <ul className="space-y-4 text-base font-normal">
              {COMPANY.divisions.map((div) => (
                <li key={div.name}>
                  <Link
                    href={div.href}
                    className="text-offwhite/60 hover:text-gold transition-all hover:translate-x-1 inline-block"
                  >
                    {div.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-24 pt-10 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8 text-[11px] font-medium premium-tracking text-white/20 uppercase">
          <p>
            &copy; {new Date().getFullYear()} {COMPANY.name}. All rights
            reserved.
          </p>
          <div className="flex space-x-10">
            <Link href="/privacy" className="hover:text-gold transition-colors">
              Privacy
            </Link>
            <Link href="/terms" className="hover:text-gold transition-colors">
              Terms
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
