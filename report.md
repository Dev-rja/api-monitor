# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 11:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.88% | 3541.7 | 10420.1 | 1000ms | 712/2087 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 136.1 | 5075.4 | 1500ms | 9/2087 |
| ❌ | `ipapi_check` | 56.88% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2087 |
| ❌ | `nasa_apod` | 78.34% | 54.62% | 2966.7 | 11152.5 | 2000ms | 947/2087 |
| ⚠️ | `dog_ceo_random` | 96.36% | 97.22% | 503.0 | 10244.1 | 2500ms | 58/2087 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.94% | 688.5 | 14877.1 | 2000ms | 43/2087 |
| ✅ | `rest_countries` | 99.28% | 98.99% | 277.4 | 10221.5 | 2500ms | 21/2087 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.4 | 10229.6 | 2500ms | 7/2087 |
| ✅ | `catfact_random` | 99.76% | 99.43% | 264.6 | 10080.2 | 3000ms | 12/2087 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.9 | 4328.4 | 1500ms | 2/2087 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.4 | 16112.2 | 2000ms | 5/2087 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.3 | 3882.8 | 2000ms | 2/2087 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5132.1 | 51.16% |
| `numbers_trivia` | 02:00 | 4598.2 | 43.75% |
| `numbers_trivia` | 10:00 | 4433.0 | 42.5% |
| `numbers_trivia` | 14:00 | 4090.2 | 39.78% |
| `numbers_trivia` | 05:00 | 4051.3 | 40.0% |
| `nasa_apod` | 05:00 | 3992.2 | 58.18% |
| `numbers_trivia` | 09:00 | 3902.6 | 37.78% |
| `numbers_trivia` | 17:00 | 3731.6 | 37.38% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `nasa_apod` | 09:00 | 3696.1 | 51.69% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
