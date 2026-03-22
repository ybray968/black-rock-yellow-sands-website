import Link from "next/link";
import Image from "next/image";
import { COMPANY } from "@/lib/siteData";

export default function Footer() {
  return (
    <footer id="contact" className="bg-forest text-offwhite border-t-4 border-gold mt-auto py-10">
      <div className="container mx-auto px-4 md:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="md:col-span-2">
            <Link href="/" className="flex items-center group gap-2 mb-6 -ml-2">
              <div className="relative h-12 w-12">
                <Image
                  src="/images/braysint-logo-large.png"
                  alt="BRAY International Logo"
                  fill
                  className="object-contain object-left"
                />
              </div>
              <div className="flex flex-col pl-0">
                <span className="font-serif font-bold text-sm tracking-wide leading-tight text-white/90">
                  BLACK ROCK AND YELLOW SANDS
                </span>
                <span className="text-[10px] tracking-widest text-gold uppercase mt-0.5">
                  International
                </span>
              </div>
            </Link>
            <p className="text-offwhite/80 max-w-sm font-normal text-sm leading-relaxed text-balance">
              Black Rock And Yellow Sands International LLC. Leading the standard in Agricultural Wholesale and Industrial Construction materials.
            </p>
          </div>

          {/* Contact Information */}
          <div>
            <h3 className="font-serif text-lg font-bold mb-6 text-gold">
              Contact Us
            </h3>
            <ul className="space-y-4 text-sm font-normal text-offwhite/80">
              <li>
                <span className="block text-xs uppercase tracking-wider text-offwhite/50 mb-1">
                  Email
                </span>
                <a
                  href={`mailto:${COMPANY.email}`}
                  className="hover:text-gold transition-colors"
                >
                  {COMPANY.email}
                </a>
              </li>
              <li>
                <span className="block text-xs uppercase tracking-wider text-offwhite/50 mb-1">
                  Phone
                </span>
                <a
                  href={`tel:${COMPANY.phone}`}
                  className="hover:text-gold transition-colors"
                >
                  {COMPANY.phone}
                </a>
              </li>
              <li>
                <span className="block text-xs uppercase tracking-wider text-offwhite/50 mb-1">
                  Location
                </span>
                <address className="not-italic">{COMPANY.address}</address>
              </li>
              <li>
                <span className="block text-xs uppercase tracking-wider text-offwhite/50 mb-1 mt-4">
                  Registration
                </span>
                <span className="opacity-80 block">CR: {COMPANY.cr}</span>
                <span className="opacity-80 block">VATIN: {COMPANY.vat}</span>
              </li>
            </ul>
          </div>

          {/* Divisions */}
          <div>
            <h3 className="font-serif text-lg font-bold mb-6 text-gold">
              Divisions
            </h3>
            <ul className="space-y-3 text-sm font-normal">
              {COMPANY.divisions.map((div) => (
                <li key={div.name}>
                  <Link
                    href={div.href}
                    className="text-offwhite/80 hover:text-gold transition-colors block"
                  >
                    {div.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-10 pt-6 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs font-normal text-offwhite/50">
          <p>
            &copy; {new Date().getFullYear()} {COMPANY.name}. All rights
            reserved.
          </p>
          <div className="flex space-x-6">
            <Link href="/privacy" className="hover:text-gold transition-colors">
              Privacy Policy
            </Link>
            <Link href="/terms" className="hover:text-gold transition-colors">
              Terms of Service
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
