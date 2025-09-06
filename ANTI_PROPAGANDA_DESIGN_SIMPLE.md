# Simplified Anti-Propaganda System

## Core Concept: 3-Layer Verification

### Layer 1: Quick AI Check
When someone submits content, AI quickly checks for:
- Obvious fake news patterns
- Emotional manipulation (ALL CAPS, excessive !!!)
- Known hoax signatures

**Output**: Risk score 0-100

### Layer 2: Community Validation
- If risk score > 50, content goes to validators
- Validators vote TRUE/FALSE/NEEDS_CONTEXT
- Must stake tokens to vote (prevents spam)
- Correct validators earn tokens, wrong ones lose tokens

### Layer 3: Final Status
Content gets one of these labels:
- ✅ VERIFIED (>70% validators say true)
- ❌ FALSE (>70% validators say false)  
- ⚠️ DISPUTED (mixed votes)
- 🔍 UNVERIFIED (not enough votes yet)

## Simple Implementation

### Smart Contract Storage
```python
claims = {
    1: {
        "ipfs_hash": "Qm123...",
        "status": "UNVERIFIED",
        "yes_votes": 0,
        "no_votes": 0,
        "total_stake": 0
    }
}
```

### Validation Rules
1. Need minimum 5 validators to vote
2. Each validator stakes 10 tokens
3. Winners split losers' tokens
4. 24 hour voting period

### Anti-Gaming Features
- Rate limit: 3 claims per day per user
- Minimum stake: 10 tokens to vote
- Reputation tracking: Bad validators get banned
- Time delay: 1 hour before public visibility

That's it. No complex multi-dimensional scoring, no specialized validator groups, no complicated consensus mechanisms. Just simple stake-based voting with basic AI pre-screening.