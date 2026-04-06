# JavaScript reference implementation:
#
# function groupByDomain(emails) {
#   const counts = {};
#   for (const email of emails) {
#     if (!email.includes('@')) continue;
#     const domain = email.split('@')[1].trim().toLowerCase();
#     if (!domain) continue;
#     counts[domain] = (counts[domain] || 0) + 1;
#   }
#   return Object.fromEntries(Object.entries(counts).sort(([a], [b]) => a.localeCompare(b)));
# }


def group_by_domain(emails: list[str]) -> dict[str, int]:
    """Example:
    >>> group_by_domain(['Alice@example.com', 'bob@EXAMPLE.com', 'invalid', 'charlie@other.org'])
    {'example.com': 2, 'other.org': 1}
    """
    counts: dict[str, int] = {}
    for email in emails:
        if '@' not in email:
            continue
        domain = email.split('@', 1)[1].strip().lower()
        if not domain:
            continue
        counts[domain] = counts.get(domain, 0) + 1

    # Return a new dict sorted by domain name (lexicographic)
    return dict(sorted(counts.items(), key=lambda item: item[0]))