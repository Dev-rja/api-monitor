# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 02:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.31% | 3399.2 | 10420.1 | 1000ms | 728/2227 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.7 | 5075.4 | 1500ms | 10/2227 |
| ❌ | `ipapi_check` | 53.39% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2227 |
| ❌ | `nasa_apod` | 79.43% | 56.62% | 2835.8 | 11152.5 | 2000ms | 966/2227 |
| ⚠️ | `dog_ceo_random` | 96.59% | 97.4% | 491.4 | 10244.1 | 2500ms | 58/2227 |
| ⚠️ | `open_meteo_weather` | 98.97% | 98.07% | 681.9 | 14877.1 | 2000ms | 43/2227 |
| ✅ | `rest_countries` | 99.33% | 99.06% | 272.2 | 10221.5 | 2500ms | 21/2227 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.3 | 10229.6 | 2500ms | 7/2227 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.9 | 10080.2 | 3000ms | 13/2227 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2227 |
| ✅ | `agify_name` | 99.91% | 99.73% | 395.2 | 16112.2 | 2000ms | 6/2227 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 187.2 | 3882.8 | 2000ms | 2/2227 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5127.8 | 51.06% |
| `numbers_trivia` | 02:00 | 4199.6 | 40.0% |
| `numbers_trivia` | 10:00 | 4179.5 | 40.0% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 09:00 | 3742.1 | 36.17% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 05:00 | 3664.7 | 36.07% |
| `nasa_apod` | 05:00 | 3662.9 | 52.46% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 09:00 | 3548.8 | 49.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
