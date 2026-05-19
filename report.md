# API Reliability Monitor — SLA Report

> Last updated: **2026-05-19 16:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.03% | 3378.4 | 10206.7 | 1000ms | 266/832 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.6 | 4595.4 | 1500ms | 4/832 |
| ❌ | `nasa_apod` | 77.04% | 57.93% | 2940.8 | 10549.1 | 2000ms | 350/832 |
| ❌ | `ipapi_check` | 82.57% | 100.0% | 154.6 | 431.8 | 2500ms | 0/832 |
| ⚠️ | `rest_countries` | 98.8% | 98.32% | 340.7 | 10221.5 | 2500ms | 14/832 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.12% | 698.6 | 14877.1 | 2000ms | 24/832 |
| ⚠️ | `dog_ceo_random` | 99.4% | 94.95% | 630.1 | 10244.1 | 2500ms | 42/832 |
| ✅ | `catfact_random` | 99.64% | 99.16% | 269.3 | 10080.2 | 3000ms | 7/832 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.8 | 253.3 | 1500ms | 0/832 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.5 | 10229.6 | 2500ms | 4/832 |
| ✅ | `agify_name` | 99.88% | 99.64% | 391.2 | 16112.2 | 2000ms | 3/832 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.1 | 3882.8 | 2000ms | 2/832 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 05:00 | 3963.3 | 37.5% |
| `numbers_trivia` | 12:00 | 3951.0 | 37.14% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `nasa_apod` | 05:00 | 3586.6 | 58.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
