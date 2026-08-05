# API Reliability Monitor — SLA Report

> Last updated: **2026-08-05 17:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.21% | 2422.1 | 10420.1 | 1000ms | 394/1729 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 130.2 | 5052.3 | 1500ms | 5/1729 |
| ❌ | `ipapi_check` | 67.21% | 99.94% | 149.4 | 4507.0 | 2500ms | 1/1729 |
| ❌ | `nasa_apod` | 78.6% | 55.64% | 2905.4 | 11152.5 | 2000ms | 767/1729 |
| ⚠️ | `dog_ceo_random` | 95.6% | 96.7% | 538.1 | 10244.1 | 2500ms | 57/1729 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.63% | 697.8 | 14877.1 | 2000ms | 41/1729 |
| ✅ | `rest_countries` | 99.13% | 98.79% | 293.2 | 10221.5 | 2500ms | 21/1729 |
| ✅ | `useless_fact` | 99.71% | 99.65% | 647.2 | 10229.6 | 2500ms | 6/1729 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.8 | 10080.2 | 3000ms | 9/1729 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1729 |
| ✅ | `agify_name` | 99.88% | 99.71% | 391.9 | 16112.2 | 2000ms | 5/1729 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.4 | 3882.8 | 2000ms | 2/1729 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4056.0 | 40.63% |
| `nasa_apod` | 03:00 | 3757.1 | 62.5% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3590.5 | 48.86% |
| `numbers_trivia` | 10:00 | 3337.8 | 31.25% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
