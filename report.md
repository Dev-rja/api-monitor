# API Reliability Monitor — SLA Report

> Last updated: **2026-05-18 22:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.8% | 3400.2 | 10206.7 | 1000ms | 266/826 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.5 | 4595.4 | 1500ms | 4/826 |
| ❌ | `nasa_apod` | 76.88% | 57.63% | 2958.9 | 10549.1 | 2000ms | 350/826 |
| ❌ | `ipapi_check` | 82.93% | 100.0% | 154.9 | 431.8 | 2500ms | 0/826 |
| ⚠️ | `rest_countries` | 98.79% | 98.31% | 341.6 | 10221.5 | 2500ms | 14/826 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.09% | 699.7 | 14877.1 | 2000ms | 24/826 |
| ⚠️ | `dog_ceo_random` | 99.39% | 94.92% | 632.2 | 10244.1 | 2500ms | 42/826 |
| ✅ | `catfact_random` | 99.64% | 99.15% | 269.2 | 10080.2 | 3000ms | 7/826 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.8 | 253.3 | 1500ms | 0/826 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.4 | 10229.6 | 2500ms | 4/826 |
| ✅ | `agify_name` | 99.88% | 99.64% | 391.8 | 16112.2 | 2000ms | 3/826 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.5 | 3882.8 | 2000ms | 2/826 |

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
