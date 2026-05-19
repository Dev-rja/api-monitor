# API Reliability Monitor — SLA Report

> Last updated: **2026-05-19 22:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.18% | 3364.1 | 10206.7 | 1000ms | 266/836 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.6 | 4595.4 | 1500ms | 4/836 |
| ❌ | `nasa_apod` | 77.15% | 57.89% | 2935.3 | 10549.1 | 2000ms | 352/836 |
| ❌ | `ipapi_check` | 82.3% | 100.0% | 154.5 | 431.8 | 2500ms | 0/836 |
| ⚠️ | `rest_countries` | 98.8% | 98.33% | 340.1 | 10221.5 | 2500ms | 14/836 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.13% | 697.7 | 14877.1 | 2000ms | 24/836 |
| ⚠️ | `dog_ceo_random` | 99.4% | 94.98% | 628.2 | 10244.1 | 2500ms | 42/836 |
| ✅ | `catfact_random` | 99.64% | 99.16% | 268.6 | 10080.2 | 3000ms | 7/836 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.7 | 253.3 | 1500ms | 0/836 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.6 | 10229.6 | 2500ms | 4/836 |
| ✅ | `agify_name` | 99.88% | 99.64% | 390.8 | 16112.2 | 2000ms | 3/836 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.9 | 3882.8 | 2000ms | 2/836 |

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
