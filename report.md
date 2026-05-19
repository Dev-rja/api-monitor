# API Reliability Monitor — SLA Report

> Last updated: **2026-05-19 01:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.87% | 3392.9 | 10206.7 | 1000ms | 266/828 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.7 | 4595.4 | 1500ms | 4/828 |
| ❌ | `nasa_apod` | 76.93% | 57.73% | 2953.1 | 10549.1 | 2000ms | 350/828 |
| ❌ | `ipapi_check` | 82.73% | 100.0% | 154.8 | 431.8 | 2500ms | 0/828 |
| ⚠️ | `rest_countries` | 98.79% | 98.31% | 341.2 | 10221.5 | 2500ms | 14/828 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.1% | 699.1 | 14877.1 | 2000ms | 24/828 |
| ⚠️ | `dog_ceo_random` | 99.4% | 94.93% | 631.6 | 10244.1 | 2500ms | 42/828 |
| ✅ | `catfact_random` | 99.64% | 99.15% | 269.1 | 10080.2 | 3000ms | 7/828 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.9 | 253.3 | 1500ms | 0/828 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.5 | 10229.6 | 2500ms | 4/828 |
| ✅ | `agify_name` | 99.88% | 99.64% | 391.3 | 16112.2 | 2000ms | 3/828 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.4 | 3882.8 | 2000ms | 2/828 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 12:00 | 4054.7 | 38.24% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `nasa_apod` | 05:00 | 3716.4 | 60.87% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
