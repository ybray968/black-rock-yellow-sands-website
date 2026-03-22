"use client";

import { COMPANY } from "@/lib/siteData";

export default function TermsOfServicePage() {
  return (
    <div className="bg-offwhite min-h-screen pt-32 pb-24">
      <div className="container mx-auto px-4 md:px-8 max-w-4xl text-forest">
        <h1 className="text-4xl md:text-5xl font-serif font-bold uppercase tracking-tighter mb-8 bg-forest text-offwhite py-6 px-8 rounded-sm">
          Terms of <span className="text-gold italic font-normal">Service.</span>
        </h1>

        <div className="space-y-8 font-normal leading-relaxed text-forest/80 text-lg text-balance">
          <p>
            <strong>Last Updated:</strong> {new Date().toLocaleDateString()}
          </p>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              1. Acceptance of Terms
            </h2>
            <p className="mb-4">
              By accessing and interacting with the {COMPANY.name} corporate
              platform, you accept and agree to be bound by the terms and provisions
              of this agreement. This website and its services are strictly designed
              for professional and corporate commercial use.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              2. Commercial Inquiries & Quotes
            </h2>
            <p className="mb-4">
              Any pricing, supply quotas, or logistical frameworks discussed or
              generated via this website do not constitute a legally binding
              contract until an official Purchase Order (PO) or Corporate Contract
              is signed by the authorized directors of {COMPANY.shortName}. International
              commodities trading (Agriculture, Construction Steel, Sulfur) is subject
              to strict market fluctuations.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              3. Compliance & Quality Assurance
            </h2>
            <p className="mb-4">
              We certify that our material exports comply with strict international
              parameters (i.e., ISO standards, surveyor testing protocols). However,
              the buyer assumes responsibility for import logistics, end-user
              compliance, and any specific national regulations of the destination
              country.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              4. Governing Law
            </h2>
            <p className="mb-4">
              Any claim relating to {COMPANY.name}'s web platform or operations
              shall be governed by the laws of the Sultanate of Oman without regard
              to its conflict of law provisions.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
